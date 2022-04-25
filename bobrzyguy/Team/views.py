from django.shortcuts import render, get_object_or_404


# Create your views here.
from Team.models import Team


def team_page(request, my_id):
    obj = get_object_or_404(Team, id=my_id)
    context = {
        'object': obj,
    }
    return render(request, "team_view.html", context)
