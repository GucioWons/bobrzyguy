from django.db import models

# Create your models here.
from django.urls import reverse

from AppUser.models import AppUser


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=80)
    boss = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(AppUser, related_name='members', blank=True)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('team:team-view', kwargs={'my_id': self.id})

    def get_join_url(self):
        return reverse('cal:join-view', kwargs={'my_id': self.id})

    def get_leave_url(self):
        return reverse('cal:leave-view', kwargs={'my_id': self.id})

class Request(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_from = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="user_from")
    user_to = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="user_to")
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField()

    def __str__(self):
        return (user_to.email + " to " + team.name)

    def get_accept_url(self):
        return reverse('team:accept-view', kwargs={'my_id': self.id})

    def get_decline_url(self):
        return reverse('team:decline-view', kwargs={'my_id': self.id})