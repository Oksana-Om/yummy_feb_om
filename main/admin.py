from django.contrib import admin
from .models import Category, Dish


admin.site.register(Dish)
admin.site.register(Category)