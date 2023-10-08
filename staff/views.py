import uuid

from django.shortcuts import render
from django.views import View

from django.conf import settings
from core.models import CustomUser
from core.email import send_email
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

        new_user = self._register_user(request)

        send_email(
            f'Hello {new_user.first_name}',
            f'your password, {new_user.password}',
            new_user.email
        )
        return self._render_login_form(request, form)

    def _render_login_form(self, request, form):
        return render(request, self.template_index, {'form': form})

    def _register_user(self, request):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password = str(uuid.uuid4())
        role = request.POST.get('role')

        if role == CustomUser.TEATCHER:
            new_user = Teacher(email=email, first_name=first_name, role=role)
        elif role == CustomUser.STAFF:
            new_user = Staff(email=email, first_name=first_name, role=role)
        elif role == CustomUser.STUDENT:
            new_user = Student(email=email, first_name=first_name, role=role)
        else:
            raise ValueError("Invalid role")

        new_user.set_password(password)
        new_user.save()
        return new_user
