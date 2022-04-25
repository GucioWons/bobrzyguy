from django.contrib import admin

# Register your models here.
from AppUser.models import AppUser

admin.site.register(AppUser)