from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    display_name = models.CharField(max_length=80, blank=True, null=True)
