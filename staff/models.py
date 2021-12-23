from django.db import models

# Create your models here.

class MonthlyBills(models.Model):
    """
    Monthly Bill Model.
    """
    month = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    bill = models.TextField(default="")

    

