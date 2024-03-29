from datetime import datetime, timedelta

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
from django.utils import timezone

from AppUser.models import AppUser
from Team.forms import CreateTeamForm
from Team.models import Team, Request
from django.db.models import Q


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def search_result_user(request):
    if request.accepts('text'):
        res = None
        series = request.POST.get('series')
        querydupa = AppUser.objects.filter(Q(email__icontains=series))
        query_se = querydupa.filter(type="WORKER")
        if len(query_se) > 0 and len(series) > 0:
            data = []
            for pos in query_se:
                item = {
                    'pk': pos.pk,
                    'email': pos.email,
                    'avatar': pos.avatar.url,

                }
                data.append(item)
            res = data
        else:
            res = 'Nie znaleziono pasojacych wynikow'

        return JsonResponse({'data': res})

    return JsonResponse({})


def search_result_team(request):
    if request.accepts('text'):
        res = None
        series = request.POST.get('series')
        query_se = Team.objects.filter(Q(name__icontains=series) | Q(description__icontains=series))
        if len(query_se) > 0 and len(series) > 0:
            data = []
            for pos in query_se:
                item = {
                    'pk': pos.pk,
                    'name': pos.name,
                    'description': pos.description,
                }
                data.append(item)
            res = data
        else:
            res = 'Nie znaleziono pasojacych wynikow'
        print(query_se)
        return JsonResponse({'data': res})
    return JsonResponse({})

def team_members_page(request, my_id):
    obj = get_object_or_404(Team, id=my_id)
    context = {
        'object': obj,
    }
    return render(request, "team_members_view.html", context)

def team_page(request, my_id):
    obj = get_object_or_404(Team, id=my_id)
    context = {
        'object': obj,
    }
    return render(request, "team_view.html", context)


def create_team_page(request):
    form = CreateTeamForm(request.POST or None)
    if form.is_valid():
        new_team = form.save(commit=False)
        new_team.boss = request.user
        new_team.save()
        return redirect(new_team.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, "create_team_view.html", context)


def invite_view(request, team_id, my_id):
    team = get_object_or_404(Team, id=team_id)
    user = get_object_or_404(AppUser, id=my_id)
    date = timezone.now() + timedelta(days=14)
    if team.boss == request.user:
        print("dupa")
        if not team.members.all().contains(user):
            Request.objects.create(user_to=user, user_from=request.user, team=team, date_expired=date)
    return redirect(team.get_absolute_url())


def notification_page(request):
    queryset = Request.objects.filter(user_to=request.user).order_by('-date_created')
    p = Paginator(queryset, 3)
    page_num = request.GET.get("page", 1)
    page = p.page(page_num)
    context = {
        'object_list': page,
    }
    return render(request, "notification_view.html", context)


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


def leave_view(request, my_id):
    obj = get_object_or_404(Team, id=my_id)
    if obj.members.all().contains(request.user):
        obj.members.remove(request.user)
    return redirect("/landing/")

def create_order(request, my_id):
    form = CreateOrderForm(request.POST or None)
