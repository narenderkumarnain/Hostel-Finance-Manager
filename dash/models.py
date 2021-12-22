"""
Model class for Students DB.
Dec 20,2021
@narender

"""
from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
# Create your models here.

class Students(models.Model):
    """
    Model class for Students DB.
    """
    roll = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField(default = 0)    

    # to be added in future for addtional features 

class Ticket(models.Model):
    """
    Model class for Tickets.
    """
    REJECTED = 'RJ'
    ACCEPTED = 'AA'
    PROCESSING = 'PS'

    STATUS_DICT = [
        (REJECTED,'Rejected'),
        (ACCEPTED,'Accepted'),
        (PROCESSING,'Processing')
    ]

    roll = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    date = models.DateTimeField(default=timezone.now) 
    amount = models.IntegerField(default=0) 
    ref_no = models.CharField(max_length = 25) 
    accepted = models.CharField(max_length=2,choices=STATUS_DICT,default = PROCESSING)
    remarks = models.TextField(max_length = 200)

    response = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.roll.roll + ' ' + str(self.date)

