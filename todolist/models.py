from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date = models.DateField()