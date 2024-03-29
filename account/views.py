from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import FormView

from config.views import common_context
from .forms import UserRegistrationForm, UserLoginForm
from .models import UserStatus


class Registration(FormView):
    template_name = "registration/reg.html"
    form_class = UserRegistrationForm
    success_url = "/login/"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Registration, self).get_context_data(**kwargs)
        context.update(common_context())

        return context

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.status = UserStatus.objects.first()
        new_user.save()
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'registration/auth.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context.update(common_context())
        context['form'] = UserLoginForm()

        return context
