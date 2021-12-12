from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Movie(models.Model):
    name = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User, related_name='movies')


    def __str__(self):
        return self.name or str(self.name)