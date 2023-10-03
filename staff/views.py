from django.shortcuts import render


def staff_home(request):
    print(f"\n ==================entrou {request}\n")

    template = 'staff_home/home.html'
    return render(request, template)
