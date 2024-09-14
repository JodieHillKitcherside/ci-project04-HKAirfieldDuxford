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
        return f"{self.departure_airfield} to {self.destination_airfield}"

