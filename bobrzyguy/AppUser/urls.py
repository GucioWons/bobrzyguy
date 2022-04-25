from django.urls import path

from AppUser.views import login_page, logout_view, landing_page, register_page, settings_page, \
    profile_page

app_name = "appuser"
urlpatterns = [
    path('login/', login_page, name='login-view'),
    path('register/', register_page, name='register-view'),
    path('logout/', logout_view, name='logout-view'),
    path('landing/', landing_page, name='landing-view'),
    path('settings/', settings_page, name='settings-view'),
    path('profile/<int:my_id>/', profile_page, name='profile-view'),
    ]