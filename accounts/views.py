"""
Views for Accounts App Routes.
Dec 19, 2021
@narender 
"""
from django.contrib.auth.models import User, auth 
from django.shortcuts import redirect, render
from accounts.forms import CustomUserCreationForm
# Create your views here.

# New User Registration View 
def registerView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            # messages to be included 
            return redirect('login')

    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request,'accounts/register.html',context)

def logoutView(request):
    auth.logout(request)
    return redirect('login')
