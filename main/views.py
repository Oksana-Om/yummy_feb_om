from django.shortcuts import render
from unicodedata import category

from .models import Category, Dish, Event, Staff
#from .models import Dish

# Create your views here.
def index(request):
    ...
    categories = Category.objects.get(pk=1)
    #events = Event.objects.get(pk=1)

    events = Event.objects.filter(is_visible=True)
    chef_member = Staff.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    context = {
        'categories': categories,
        'events': events,
        'chef_member': chef_member,
    }
    return render(request, 'index.html', context=context)
