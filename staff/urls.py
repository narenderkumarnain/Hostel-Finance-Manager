"""
URL for Staff features.
Dec 23,2021
@narender
"""
from django.urls import path 
from staff.views import homeView, billUpload, listStaffTickets, TicketDetailView, ticketDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload-bill/', billUpload, name = 'bill-upload' ),
    path("resolve-tickets/", listStaffTickets, name="resolve-tickets"),
    path('ticket/detail/<int:pk>/', ticketDetailView, name = 'staff-ticket-detail'),
    # path("not-allowed/", notAllowed, name="not-allowed"),
    path('', homeView, name = "staff-home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)