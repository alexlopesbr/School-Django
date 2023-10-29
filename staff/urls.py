from django.urls import path

from .views import RegisterUser, UserList

urlpatterns = [
    path('home', RegisterUser.as_view(), name='staff_home'),
    path('user-list', UserList.as_view(), name='staff_user_list'),
]
