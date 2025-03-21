from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.groups.filter(name='manager').exists()
@login_required(login_url='login')
@user_passes_test(is_manager)
# Create your views here.
def index(request):
    return HttpResponse("Manager Page")
