from django.shortcuts import render


def staff_home(request):
    template = 'staff/home.html'
    return render(request, template)
