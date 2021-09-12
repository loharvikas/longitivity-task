from django.db import models
from users.models import User


class Parameter(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Organisation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parameters = models.ManyToManyField(Parameter, blank=True)

    def __str__(self):
        return f"{self.user.username} | {self.name}"
