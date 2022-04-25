from django.urls import path

from Team.views import team_page

app_name = "team"
urlpatterns = [
    path('team/<int:my_id>/', team_page, name='team-view'),
    ]