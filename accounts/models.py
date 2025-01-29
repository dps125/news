from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)