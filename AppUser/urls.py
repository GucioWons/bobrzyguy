from django.urls import path

from AppUser.views import logout_view, landing_page, settings_page, \
    profile_page, logister_page, search_page

app_name = "appuser"
urlpatterns = [
    path('logister/', logister_page, name='logister-view'),
    path('logout/', logout_view, name='logout-view'),
    path('landing/', landing_page, name='landing-view'),
    path('settings/', settings_page, name='settings-view'),
    path('profile/<int:my_id>/', profile_page, name='profile-view'),
    path('search_all', search_page, name='search-view'),
    ]