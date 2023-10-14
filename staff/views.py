import uuid

from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.contrib import messages

from core.cache import CachedData
from core.models import CustomUser
from core.email import send_email
from staff.forms import UserRegister, UserList

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
            message = 'invalid form'
            return self._render_login_form(request, form, message=message)

        new_user = self._register_user(request)

        if new_user is None:
            message = 'Problems to save user'
            return self._render_login_form(request, form, message=message)

        send_email(
            f'Hello {new_user.first_name}',
            f'your password, {new_user.password}',
            new_user.email
        )
        message = 'User created successfully.'
        return self._render_login_form(request, form, message=message)

    def _render_login_form(self, request, form, message = None):
        context = {'form': form, 'message': message}
        return render(request, self.template_index, context)

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
            return None

        new_user.set_password(password)
        # new_user.save()
        return new_user

class UserList(View):
    form_class = UserList
    template_index = 'staff/list_user.html'

    users = CachedData(
        'cached_users',
        CustomUser,
        300
    ).cache_model()

    def get(self, request, *args, **kwargs):

        form = self.form_class()
        return self._render_user_list_form(request, form, users=self.users)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            message = 'invalid form'
            return self._render_user_list_form(request, form, users=self.users, message=message)
        return self._render_user_list_form(request, form, users=self.users)

    def _render_user_list_form(self, request, form, message=None, users=None):
        role = request.POST.get('role')

        if role in [role[1] for role in CustomUser.ROLE_CHOICES]:
            users = [user for user in users if user.role == role]

        context = {
            'form': form,
            'message': message,
            'users': users
        }
        return render(request, self.template_index, context)
