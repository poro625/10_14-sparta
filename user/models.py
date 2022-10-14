from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile = models.TextField(max_length=500, blank=True)
    telnumber = models.IntegerField(max_length=500, blank=False)
    address = models.TextField(max_length=500, blank=True)

