from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.detail import DetailView
from staff.forms import MonthlyBillForm
from dash.models import Students, Ticket
from accounts.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Sum 
from django.utils.datastructures import MultiValueDictKeyError
import threading
from staff.utils import process_csv
from django.utils import timezone 

# Create your views here.

def updateStudentRecords(processed_csv,month):
    for (roll_no,amount) in processed_csv:
        try:
            student = Students.objects.get(roll = CustomUser.objects.get(roll = roll_no))
        except ObjectDoesNotExist:
            continue 

        # Updating the Amount
        student.amount += amount 
        student.latest_bill = month 
        student.latest_amount = amount 

        # Saving the Changes in the Database 
        student.save()

     

@login_required
def homeView(request):
    if not request.user.is_staff:
        return redirect('not-allowed')
    # preparing context object with some aggregate stats
    no_students = CustomUser.objects.filter(is_staff = False).count()
    remaining_total = Students.objects.filter(amount__gte = 0).aggregate(Sum('amount'))['amount__sum']
    extra = Students.objects.filter(amount__lt = 0).aggregate(Sum('amount'))['amount__sum']
    net = Students.objects.all().aggregate(Sum('amount'))['amount__sum']

    pending_tickets = Ticket.objects.filter(accepted = "PS").count()

    
    context  = {
        'no_students': no_students,
        'remaining_total': remaining_total,
        'extra': extra ,
        'net': net,
        'pending_tickets': pending_tickets,
    }

    return render(request,'staff/home.html',context)

@login_required
def billUpload(request):
    if not request.user.is_staff:
        return redirect('not-allowed')

    if request.method == "POST":
        form = MonthlyBillForm(request.POST)
        
        
        if form.is_valid():
            bill_str = request.FILES['bill'].read()
            form.instance.bill = bill_str
            print(bill_str)
            processed_csv = process_csv(bill_str)

            thread_update = threading.Thread(target=updateStudentRecords,args=(processed_csv,form.instance.month))

            form.save()
            thread_update.start()
            messages.success(request,"Student Records will be updated with latest Bill Shortly")
            # t.join()
            return redirect('staff-home')
    else:
        form = MonthlyBillForm()
    
    context = {
        'form': form,
    }
    return render(request,'staff/upload_bill.html',context)


@login_required
def listStaffTickets(request):
    if not request.user.is_staff:
        return redirect('not-allowed')
    context = {}
    tickets = Ticket.objects.filter(accepted = "PS").order_by('date')
    context['tickets'] = tickets
    return render(request,'staff/list_tickets.html',context)


class TicketDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Ticket 
    
    def test_func(self):
        ticket = self.get_object()
        if (self.request.user.is_staff is False):
            return False
        return True

@login_required
def ticketDetailView(request,pk):
    if not request.user.is_staff:
        return redirect('not-allowed')
    object_ob = Ticket.objects.get(id = pk)
    context = {}    
    try:
        latest_ticket = Ticket.objects.filter(roll = object_ob.roll, accepted = 'AA').order_by('acceptance_date').reverse()[0]
    except IndexError:
        latest_ticket = {
            'date': "" ,
            'amount': 0 ,
            'ref_no': ""
        }
    context['object'] = object_ob
    context['latest'] = latest_ticket

    if request.method == "POST":
        print(request.POST)
        try:
            option = request.POST['inlineRadioOptions']
        except MultiValueDictKeyError:
            messages.error(request, "Please select a Accepted/Rejected Option")
            return render(request,'staff/ticket_detail.html', context)
        text_response = request.POST['text-response']

        if option == 'option1':
            object_ob.accepted = Ticket.ACCEPTED
            object_ob.roll.students.amount -= object_ob.amount 
            object_ob.acceptance_date = timezone.now()
            if text_response == '':
                object_ob.response = "Your Ticket is Accepted." 
            else:
                object_ob.response = text_response

        elif option == 'option2':
            object_ob.accepted = Ticket.REJECTED
            if text_response == '':
                object_ob.response = "Your Ticket is Rejected." 
            else:
                object_ob.response = text_response
            object_ob.acceptance_date = timezone.now()

        object_ob.save()
        object_ob.roll.students.save()
        return redirect('resolve-tickets')
    
    return render(request,'staff/ticket_detail.html', context)
    
