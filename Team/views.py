from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from AppUser.models import AppUser
from Team.models import Team, Request


def team_page(request, my_id):
    obj = get_object_or_404(Team, id=my_id)
    context = {
        'object': obj,
    }
    return render(request, "team_view.html", context)

def invite_view(request, team_id, my_id):
    team = get_object_or_404(Team, id=team_id)
    user = get_object_or_404(AppUser, id=my_id)
    date = datetime.now() + datetime.timedelta(days=14)
    if team.boss == request.user:
        if not team.members.all().contains(user):
            Request.objects.create(user_to=user, user_from=request.user, team=team, date_expired=date)
    return redirect(team.get_absolute_url())

def accept_view(request, my_id):
    obj = get_object_or_404(Request, id=my_id)
    if request.user == obj.user_to:
        if not obj.accepted and not obj.declined:
            if obj.date_expired > timezone.now():
                obj.accepted = True
                obj.save()
                obj.team.members.add(obj.user_to)
                return redirect(obj.team.get_absolute_url())
    return redirect("/landing/")

def decline_view(request, my_id):
    obj = get_object_or_404(Request, id=my_id)
    if request.user == obj.user_to:
        if not obj.accepted and not obj.declined:
            if obj.date_expired > timezone.now():
                obj.declined = True
                obj.save()
                return redirect("/landing/")
    return redirect("/landing/")