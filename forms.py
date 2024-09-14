from django import forms
from .models import Booking, Payment

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Booking
        fields = ['flight', 'aircraft', 'date']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method']