from django.urls import path

from .views import RegisterUser, UserList, UserEdit

urlpatterns = [
    path('home', RegisterUser.as_view(), name='staff_home'),
    path('user-list', UserList.as_view(), name='staff_user_list'),
    path('user-edit', UserEdit.as_view(), name='staff_user_edit'),
]
