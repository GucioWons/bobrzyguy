from django.contrib import admin

# Register your models here.
from Team.models import Team, Request, Opinion, Order

admin.site.register(Team)
admin.site.register(Request)
admin.site.register(Opinion)
admin.site.register(Order)

