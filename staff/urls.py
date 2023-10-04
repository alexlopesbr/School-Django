from django.urls import path

import staff.views as staff_views

urlpatterns = [
    path('home', staff_views.staff_home, name='staff_home'),
]
