"""
Forms for Custom User Model.
Dec 19, 2021 
@narender 

"""
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from django.contrib.auth.models import User
from accounts.models import CustomUser

# Class for User Creation
class CustomUserCreationForm(UserCreationForm):
    """
    Class for Custom User Creation Form.
    """
    class Meta:
        model = CustomUser
        fields = ['roll', 'email','name', 'password1', 'password2']

# Class for User Change Form
class CustomUserChangeForm(UserChangeForm):
    """
    Class for Custom User Change Form.
    """
    class Meta:
        model = CustomUser
        fields = ['email',] 
        


