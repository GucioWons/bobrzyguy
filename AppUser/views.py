from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
from oauthlib.oauth2.rfc6749.errors import LoginRequired

from AppUser.forms import SignUpForm, AppUserCreateForm
from AppUser.models import AppUser


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/login/')
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "login_view.html", context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    form = SignUpForm(request.POST or None)
    form2 = AppUserCreateForm(request.POST or None)
    if form.is_valid() and form2.is_valid():
        user = form.save()
        AppUser.objects.create(user=user, type=form2.cleaned_data.get("type"))
        login(request, user)
        return redirect("/login/")
    context = {
        "form": form,
        "form2": form2
    }
    return render(request, "register_view.html", context)

