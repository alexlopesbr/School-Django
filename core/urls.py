from django.urls import path

from . import views
import staff.views as staff_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('staff/home', staff_views.staff_home, name='staff_home'),

]
