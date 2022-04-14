from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm

from AppUser.models import AppUser


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password'
    }))  # help-text
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = AppUser
        fields = ('type', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))


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
