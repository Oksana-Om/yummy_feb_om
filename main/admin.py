from django.contrib import admin
from .models import Category, Dish, Event, Staff

admin.site.register(Dish)
admin.site.register(Event)
admin.site.register(Staff)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
