from django.urls import path

from Team.views import team_page, invite_view, accept_view

app_name = "team"
urlpatterns = [
    path('team/<int:my_id>/', team_page, name='team-view'),
    path('invite/<int:team_id>/<int:my_id>/', invite_view, name='invite-view'),
    path('accept/<int:my_id>/', accept_view, name='accept-view'),
    ]