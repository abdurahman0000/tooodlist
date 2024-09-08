from django.db import models
from django.db.models import TextField


class Task(models.Model):
    title = models.CharField(max_length=100)
    descriptions = TextField()
    complated = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
