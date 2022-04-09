from django.urls import path

from AppUser.views import login_page

app_name = "appuser"
urlpatterns = [
    path('login/', login_page, name='login-view'),
    ]