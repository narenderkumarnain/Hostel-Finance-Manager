from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from dash.forms import TicketCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView ,
    UpdateView ,
    DeleteView 
)
from dash.models import Ticket
from django.urls import reverse
# Create your views here.

@login_required
def homeView(request):
    if request.user.is_staff:
        return redirect('staff-home')
    context = {}
    tickets = Ticket.objects.filter(roll = request.user).order_by('date').reverse()[:5]
    context['tickets'] = tickets
    return render(request,'dash/home.html',context)

def listStudentTickets(request):
    context = {}
    tickets = Ticket.objects.filter(roll = request.user).order_by('date').reverse()
    context['tickets'] = tickets
    return render(request,'dash/all_tickets.html',context)


class RaiseTicketView(LoginRequiredMixin,CreateView):
    model = Ticket
    fields = ['amount','ref_no','remarks',]

    def form_valid(self,form):
        form.instance.roll = self.request.user 
        return super().form_valid(form) 
    
    def get_success_url(self) -> str:
        return reverse('home')

class TicketUpdateViewStudent(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Ticket 
    fields = ['amount', 'ref_no', 'remarks',] 

    def form_valid(self,form):
        form.instance.roll = self.request.user 
        return super().form_valid(form) 

    def test_func(self):
        ticket = self.get_object()
        if ticket.roll == self.request.user:
            return True 
        else:
            return False 

    def get_success_url(self) -> str:
        return reverse('home')

class TicketDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Ticket
    success_url = '/ticket/all/student/'

    def test_func(self):
        ticket = self.get_object()
        if ticket.roll != self.request.user:
            return False

        # Only Processing Posts can be deleted 
        if ticket.accepted != "PS":
            return False 
        return True 

class TicketDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Ticket 
    
    def test_func(self):
        ticket = self.get_object()
        if (ticket.roll != self.request.user) and (self.request.user.is_staff is False):
            return False
        
        return True



