
from django.http import HttpResponse
from django.shortcuts import render, redirect
from unicodedata import category
from django.contrib import messages



from .models import Category, Dish, Event, Staff
from .forms import ReservationForm

# Create your views here.
def index(request):
    ...
    categories = Category.objects.get(pk=1)
    #events = Event.objects.get(pk=1)

    events = Event.objects.filter(is_visible=True)
    chef_member = Staff.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    reservation = ReservationForm(request.POST or None)
    if request.method == 'POST' and reservation.is_valid():
        reservation.save()
        messages.success(request, 'Your reservation has been saved. Wait for a call')

        return redirect('home')

    context = {
        'categories': categories,
        'events': events,
        'chef_member': chef_member,
        'reservation': reservation,


    }
    return render(request, 'index.html', context=context)
