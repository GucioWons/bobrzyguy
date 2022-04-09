from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect


# Create your views here.

from AppUser.forms import SignUpForm, AppUserCreateForm
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
    form2 = AppUserCreateForm(request.POST or None)
    if form.is_valid() and form2.is_valid():
        user = form.save()
        AppUser.objects.create(user=user, type=form2.cleaned_data.get("type"))
        login(request, user)
        return redirect("/landing/")
    context = {
        "form": form,
        "form2": form2
    }
    return render(request, "register_view.html", context)

@login_required(login_url='/landing')
def logout_view(request):
    logout(request)
    return redirect("/landing/")

def landing_page(request):
    return render(request, "landing_view.html")

@login_required(login_url='/landing')
def change_password_page(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)  # Important!
        return redirect('/changepassword/')
    context = {
        "form": form,
    }
    return render(request, 'change_password_view.html', context)
