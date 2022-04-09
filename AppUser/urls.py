from django.urls import path

from AppUser.views import login_page, register_page, logout_view, landing_page, change_password_page

app_name = "appuser"
urlpatterns = [
    path('login/', login_page, name='login-view'),
    path('register/', register_page, name='register-view'),
    path('logout/', logout_view, name='logout-view'),
    path('landing/', landing_page, name='landing-view'),
    path('changepassword/', change_password_page, name='change-password-view')
    ]