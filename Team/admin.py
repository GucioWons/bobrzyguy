from django.contrib import admin

# Register your models here.
from Team.models import Team, Request

admin.site.register(Team)
admin.site.register(Request)