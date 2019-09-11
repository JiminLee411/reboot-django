from django.db import models

# Create your models here.
class PastLife(models.Model):
    name = models.TextField(max_length=10)
    age = models.IntegerField()
    myjob = models.TextField(max_length=50)