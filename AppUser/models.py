from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AppUser(models.Model):
    TYPE_CHOICES = [('CUSTOMER', 'Customer'), ('WORKER', 'Worker')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.user.username
