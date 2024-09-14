from django.urls import path
from . import views 

urlpatterns - [
    path('', views.home, name='home'),
    path('flights/' views.flights_options, name='flight_options'),
    path('booking/<int:flight_id>/' views.booking_view, name='booking'),
    path('payment/<int:booking_id>/' views.payment_view, name='payment'),
    path('confirmation/<int:booking_id>/' views.confirmation_view, name='confirmation'),
]