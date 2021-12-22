"""
Forms for Models.
Dec 22, 2021
@narender
"""
from django.forms import ModelForm
from dash.models import Ticket

class TicketCreationForm(ModelForm):
    """
    Form class for Ticket Model.
    """
    class Meta:
        model = Ticket
        fields = ['amount','ref_no','remarks',]