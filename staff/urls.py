from django.urls import path

from .views import staff_home

urlpatterns = [
    path('home', staff_home, name='staff_home'),
]
