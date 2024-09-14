from django.contrib import admin
from .models import Aircraft, FlightOption, Booking, Payment

admin.site.register(Aircraft)
admin.site.register(FlightOption)
admin.site.register(Booking)
admin.site.register(Payment)