from staff.models import MonthlyBills
from django import forms 

class MonthlyBillForm(forms.ModelForm):
    class Meta:
        model = MonthlyBills
        fields = ['month',]