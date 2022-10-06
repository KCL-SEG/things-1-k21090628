from django.db import models
from django.db.models import Model

class Thing(Model):
    name = models.TextField()
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
