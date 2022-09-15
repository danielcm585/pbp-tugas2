from django.db import models

class MyWatchList(models.Model):
  watched = models.BooleanField(default=False)
  title = models.CharField(max_length=100)
  rating = models.IntegerField()
  release_date = models.DateTimeField(auto_now_add=True, blank=True)
  review = models.TextField()