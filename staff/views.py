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
        context = {'form': form}
        return render(request, self.template_index, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            message = 'invalid form'
            context = {'form': form, 'message': message}
            return render(request, self.template_index, context)

        new_user = self._register_user(request)

        if new_user is None:
            message = 'Problems to save user'
            context = {'form': form, 'message': message}
            return render(request, self.template_index, context)

        send_email(
            f'Hello {new_user.first_name}',
            f'your password, {new_user.password}',
            new_user.email
        )
        message = 'User created successfully.'
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
        new_user.save()
        return new_user


class UserList(View):
    form_class = UserList
    template_index = 'staff/list_user.html'

    def get(self, request, *args, **kwargs):
        role_filter = request.GET.get('role')

        users = self.filter_users_by_role_choice(role_filter)

        form = self.form_class()
        context = {'form': form, 'users': users}
        return render(request, self.template_index, context)


    def filter_users_by_role_choice(self, role_filter):
        users = CachedData(
            'cached_users',
            CustomUser,
            300
        ).cache_model()

        # filter only by the valid choices excluding as example the choice all
        if role_filter in [role[1] for role in CustomUser.ROLE_CHOICES]:
            return [user for user in users if user.role == role_filter]
        return users
