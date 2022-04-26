from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm

from AppUser.models import AppUser


class SignUpForm(UserCreationForm):
    TYPE_CHOICES = [('CUSTOMER', 'Customer'), ('WORKER', 'Worker')]

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'input',
        'type': 'password'
    }))  # help-text
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    type = forms.ChoiceField(choices=TYPE_CHOICES)

    class Meta:
        model = AppUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'type')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password'}))


class ChangeFirstNameForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'text'}))
    class Meta:
        model = User
        fields = ('first_name',)


class ChangeLastNameForm(ModelForm):
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'text'}))
    class Meta:
        model = User
        fields = ('last_name',)


class ChangeEmailForm(ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input', 'type': 'text'}))
    class Meta:
        model = User
        fields = ('email',)
