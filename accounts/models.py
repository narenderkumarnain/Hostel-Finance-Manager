"""
Custom User Model for Project.
Dec 19, 2021
@narender

"""
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager
# Create your models here.


# Class for Custom User 
class CustomUser(AbstractUser):
    """
    Model class for Custom User Model.
    """
    username = None 
    roll = models.CharField(max_length=8, unique=True)  
    email = models.EmailField(_("email address"), max_length=254)
    name = models.CharField(max_length=50,blank=True) 

    USERNAME_FIELD = "roll" 
    REQUIRED_FIELDS = ['email','name'] 

    objects = CustomUserManager() 

    def __str__(self):
        return self.roll 
