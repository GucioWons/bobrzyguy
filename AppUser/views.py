from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from AppUser.forms import SignUpForm, ChangePasswordForm, ChangeFirstNameForm, ChangeLastNameForm, ChangeEmailForm
from AppUser.models import AppUser


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/landing/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/landing/')
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "login_view.html", context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/landing/')
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("/landing/")
    context = {
        "form": form,
    }
    return render(request, "register_view.html", context)


@login_required(login_url='/landing')
def logout_view(request):
    logout(request)
    return redirect("/landing/")


def landing_page(request):
    return render(request, "landing_view.html")


def settings_page(request):
    form = ChangeFirstNameForm(instance=request.user)
    form2 = ChangeLastNameForm(instance=request.user)
    form3 = ChangeEmailForm(instance=request.user)
    form4 = ChangePasswordForm(request.user)
    response = redirect('appuser:settings-view')
    if request.method == 'POST':
        if 'change_first_name' in request.POST:
            form = ChangeFirstNameForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return response
        elif 'change_last_name' in request.POST:
            form2 = ChangeLastNameForm(request.POST, instance=request.user)
            if form2.is_valid():
                form2.save()
                return response
        elif 'change_email' in request.POST:
            form3 = ChangeEmailForm(request.POST, instance=request.user)
            if form3.is_valid():
                form3.save()
                return response
        elif 'change_password' in request.POST:
            form4 = ChangePasswordForm(request.user, request.POST)
            if form4.is_valid():
                user = form4.save()
                update_session_auth_hash(request, user)  # Important!
                return response
    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'form4': form4
    }
    return render(request, "settings_view.html", context)

@login_required(login_url='/landing')
def profile_page(request, my_id):
    obj = get_object_or_404(AppUser, id=my_id)
    context = {
        'object': obj,
    }
    return render(request, "profile_view.html", context)