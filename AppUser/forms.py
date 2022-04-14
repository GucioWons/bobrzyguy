from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm

from AppUser.models import AppUser

TYPE_CHOICES = [('CUSTOMER', 'Customer'), ('WORKER', 'Worker')]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

class AppUserCreateForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ('type',)

class ChangeFirstNameForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name',)

class ChangeLastNameForm(ModelForm):
    class Meta:
        model = User
        fields = ('last_name',)

class ChangeEmailForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)
