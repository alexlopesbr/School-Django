from django.urls import path

from .views import Home, UserList

urlpatterns = [
    path('home', Home.as_view(), name='staff_home'),
    path('user-list', UserList.as_view(), name='staff_user_list'),
]
