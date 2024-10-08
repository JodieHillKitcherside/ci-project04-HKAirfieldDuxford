from django.shortcuts import render, get_object_or_404, redirect 
from django.urls import reverse
from .models import Aircraft, FlightOption, Booking
from .forms import BookingForm, PaymentForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login required

def home(request):
    return render(request, 'home.html')

def flight_options(request):
    flights = FlightOption.objects.all()
    return render(request, 'flight_options.html', {'flights': flights})

@login_required
def booking_view(request, flight_id):
    flight = get_object_or_404(FlightOption, id=flight_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is.valid():
            booking = form.save(commit=False)
            booking.user = request.userbooking.save()
            return redirect('payment', booking_id=booking.id)
        
        else:
            form = BookingForm(inital={'flight': flight})
        return render(request, 'booking.html', {'form': form, 'flight': flight})
    pass

@login_required
def payment_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is.valid():
            payment = form.save(commit=False)
            pament.booking = booking
            payment.save()
            booking.payment_staus = True
            booking.save()
            return redirect('confirmation', booking_id=booking.id)
        
        else:
            form = PaymentForm(initial={'amount': booking.total_cost})
        return render(request, 'payment.html', {'form': form, 'booking': booking})
pass 

def confirmation_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return(request, 'confirmation.html', {'booking': booking})

def register(request):
    if request.method == 'POST':
        from = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        else:
            form = UserRegistrationForm
        return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


