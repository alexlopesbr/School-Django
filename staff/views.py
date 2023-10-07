from django.shortcuts import render
from django.views import View

from staff.forms import UserRegister

from teacher.models import Teacher

class Home(View):
    form_class = UserRegister
    template_index = 'staff/home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self._render_login_form(request, form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self._render_login_form(request, form)

        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        role = request.POST.get('role')

        new_user = Teacher(email=email, first_name=first_name, role=role)
        new_user.set_password('ale123456')
        new_user.save()


    def _render_login_form(self, request, form):
        return render(request, self.template_index, {'form': form})
