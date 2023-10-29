from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from . models import CustomUser
from . forms import LoginForm


class Login(View):
    STAFF_HOME_URL = '/staff/user-list'
    STUDENT_HOME_URL = '/student/home'
    TEACHER_HOME_URL = '/teacher/home'

    form_class = LoginForm
    template_index = 'index/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self._render_login_form(request, form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self._render_login_form(request, form)

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is None:
            return self._render_login_form(request, form)

        login(request, user)
        return self._redirect_based_on_user_role(user)

    def _render_login_form(self, request, form):
        return render(request, self.template_index, {'form': form})

    def _redirect_based_on_user_role(self, user):
        if user.role == CustomUser.STAFF:
            return HttpResponseRedirect(self.STAFF_HOME_URL)
        elif user.role == CustomUser.STUDENT:
            return HttpResponseRedirect(self.STUDENT_HOME_URL)
        elif user.role == CustomUser.TEATCHER:
            return HttpResponseRedirect(self.TEACHER_HOME_URL)


def logout_user(request):
    logout(request)
    form_class = LoginForm
    template_index = 'index/index.html'
    return render(request, template_index, {'form': form_class})
