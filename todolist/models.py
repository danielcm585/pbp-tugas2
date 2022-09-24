from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  done = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField(auto_now=True)
  title = models.CharField(max_length=200)
  description = models.TextField()
  