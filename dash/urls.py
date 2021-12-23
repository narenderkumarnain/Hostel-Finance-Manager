"""
URL patterens for Dash App.
Dec 20, 2021
@narender

"""
from django.urls import path
from dash.views import (homeView,
             RaiseTicketView,
              TicketUpdateViewStudent,
              listStudentTickets,
              TicketDeleteView,
              TicketDetailView)

urlpatterns = [
    path('ticket/all/student/',listStudentTickets,name = 'list-student-tickets' ),
    path('ticket/delete/<int:pk>/', TicketDeleteView.as_view(template_name = "dash/delete_view.html"), name = 'delete_ticket_student'),
    path('ticket/update/student/<int:pk>/', TicketUpdateViewStudent.as_view(template_name = 'dash/update_ticket.html'), name = 'update_ticket_student'),
    path('ticket/detail/<int:pk>/', TicketDetailView.as_view(template_name = 'dash/detail_ticket.html'), name = 'detail_ticket'),
    path('ticket/raise/', RaiseTicketView.as_view(template_name = 'dash/raise_ticket.html'), name = 'raise'),
    path('', homeView, name = 'home'),
]