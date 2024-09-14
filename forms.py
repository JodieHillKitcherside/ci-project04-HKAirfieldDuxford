from django import forms
from .models import Booking, Payment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Booking
        fields = ['flight', 'aircraft', 'date']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Userfields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True)
    user = super(UserRegistrationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.save()
    return user