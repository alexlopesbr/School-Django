from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def index(request):
    index_template = 'index/index.html'
    return render(request, index_template)


def login_user(request):
    home_template = 'home/home.html'
    index_template = 'index/index.html'

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, home_template)
    return render(request, index_template)


def logout_user(request):
    logout(request)
    index_template = 'index/index.html'
    return render(request, index_template)
