from django.urls import path

from Team.views import team_page, invite_view, accept_view, decline_view, leave_view, create_team_page, \
    notification_page, search_result_team, team_members_page

app_name = "team"
urlpatterns = [
    path('team/<int:my_id>/', team_page, name='team-view'),
    path('team/invite/<int:team_id>/<int:my_id>/', invite_view, name='invite-view'),
    path('accept/<int:my_id>/', accept_view, name='accept-view'),
    path('decline/<int:my_id>/', decline_view, name='decline-view'),
    path('leave/<int:my_id>/', leave_view, name='leave-view'),
    path('team/create/', create_team_page, name='create-team-view'),
    path('notifications/', notification_page, name='notification-view'),
    path('searchteam/', search_result_team, name='search'),
    path('team/<int:my_id>/members/', team_members_page, name='members-view')
    ]
