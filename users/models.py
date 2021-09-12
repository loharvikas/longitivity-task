from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    first_name = None
    last_name = None
