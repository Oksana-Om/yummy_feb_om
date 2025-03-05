from django.shortcuts import render
from unicodedata import category

from .models import Category, Dish
#from .models import Dish

# Create your views here.
def index(request):
    ...
    #categories = Category.objects.all()
    #categories = Category.objects.filter(is_visible=True)
    categories = Category.objects.get(pk=1)
    #categories = Category.objects.filter()
    #categories = Category.objects.last()
    categories = Category.objects.get(pk=1)
   # dishes_by_category = Dish.objects.filter(category=categories, is_visible=True)
    #for dish in categories.dishes.all():
    #for dish in categories:
     #   print(dish)
    #print()
   # pass
    categories = Category.objects.filter(is_visible=True)
    context = {
        'categories': categories,
    }
    return render(request, 'index.html')