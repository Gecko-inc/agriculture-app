from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _


class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'reg-form_email _req _email', 'type': "email",
                                                 "placeholder": "Электронная почта*",
                                                 'required': "True"})

        self.fields['password'].widget.attrs.update({'class': 'password1 _req', 'type': "password",
                                                 "placeholder": "Пароль",
                                                 'required': "True"})

        self.fields['password2'].widget.attrs.update({'class': 'password2 _req', 'type': "password",
                                                 "placeholder": "Повторите пароль",
                                                 'required': "True"})

    password = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Подтвердите пароль'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(_('Пароли не совпадают'))
        return cd['password2']


class UserLoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'auth-form_email _req _email', 'type': "email",
                                                 "placeholder": "Электронная почта*",
                                                 'required': "True"})

        self.fields['password'].widget.attrs.update({'class': 'password _req', 'type': "password",
                                                     "placeholder": "Пароль",
                                                     'required': "True"})

    password = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)
