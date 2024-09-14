from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class Aircaft(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capaicty = models.IntegerField()
    cost_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.name 

class FlightOption(models.Model):
    aircraft = models.ForeginKey(Aircaft, on_delete=models.CASCASE)
    departure_airfield = models.CharField(max_length=100)
    destination_airfield = models.DurationField()

    def _str_(self):
        return f"{self.departure_airfield} to {self.destination_airfield}

class Booking(models.Model):
    user = models.ForeginKey(User, on_delete=models.CASCADE)
    flight = models.ForeginKey(User, on_delete=models.CASCADE)
    aircraft = models.ForeginKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)

    def get_total_cost(self):
        return self.aircraft.cost_per_hour * self.flight.flight_duration.total_seconds()/ 3600

    def save(self, *args, **kwargs):
        self.total_cost = self.get._total_cost()
        super().save(*args, **kwargs)
    
    def _str_(self):
        return f"Booking {self.id} by {self.user.name}" 

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def _str_(self):
        return f"Payment {self.id} for Booking {self.booking.id}"