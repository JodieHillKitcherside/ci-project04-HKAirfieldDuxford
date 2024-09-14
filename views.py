from django.shortcuts import render, get_object_or_404, redirect 
from django.urls import reverse
from .models import Aircraft, FlightOption, Booking
from .forms import BookingForm, PaymentForm

def home(request):
    return render(request, 'home.html')

def flight_options(request):
    flights = FlightOption.objects.all()
    return render(request, 'flight_options.html', {'flights': flights})

def booking_view(request, flight_id):
    flight = get_object_or_404(FlightOption, id=flight_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is.valid():
            booking = form.save(commit=False)
            booking.user = request.userbooking.save()
            return redirect('payment', booking_id=booking.id)
        
        else:
            form = BookingForm(inital='{flight': flight})
        return render(request, 'booking.html', {'form': form, 'flight': flight})

        