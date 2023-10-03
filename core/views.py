from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from . models import CustomUser
from staff.views import staff_home


def index(request):
    index_template = 'index/index.html'
    return render(request, index_template)


def login_user(request):
    index_template = 'index/index.html'

    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        if user.role == CustomUser.STAFF:
            return staff_home(request)
    return render(request, index_template)


def logout_user(request):
    logout(request)
    index_template = 'index/index.html'
    return render(request, index_template)
