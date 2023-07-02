from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Fish(models.Model):
    scientific_name = models.CharField(max_length=255)
    common_names = ArrayField(models.CharField(max_length=50))
    description = models.TextField()
    min_fish_size = models.FloatField()
    max_fish_size = models.FloatField()
    min_tank_size = models.FloatField()
    max_tank_size = models.FloatField()

class Result(models.Model):
    fish_id = models.ForeignKey(to=Fish, on_delete=models.CASCADE)