from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator




class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_categories'
        ordering = ('sort', 'name')
        verbose_name = 'Категорія страв'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def __iter__(self):
        for dish in self.dishes.all():
            yield dish


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    desc = models.TextField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='dishes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_dishes'
        ordering = ('sort', 'name')
        verbose_name = 'Страва'
        verbose_name_plural = 'dishes'

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    desc = models.TextField(max_length=1000, unique=True)
    photo = models.ImageField(upload_to='events/')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_events'

    def __str__(self):
        return self.name

class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=40)
    desc = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='staff/')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name

class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

class Contact(models.Model):
    address = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    desc = models.TextField(max_length=500)

    class Meta:
        db_table = 'contact'

class Contacts(models.Model):
    address = RichTextField()
    reservations = RichTextField()
    opening_hours = RichTextField()

class Reservations(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(38)?\d{10}$',)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50, validators=[phone_regex])
    date = models.DateField()
    time = models.TimeField()
    number_guests = models.PositiveIntegerField(default=1)
    message = models.TextField(max_length=255)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'main_reservations'
        ordering = ('-date_created',)





