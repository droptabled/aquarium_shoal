from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Fish(models.Model):
    scientific_name = models.CharField(max_length=255)
    common_names = ArrayField(models.CharField(max_length=50))
    description = models.TextField(null=True)
    min_fish_size = models.FloatField(null=True)
    max_fish_size = models.FloatField(null=True)
    min_tank_size = models.FloatField(null=True)
    max_tank_size = models.FloatField(null=True)

    def common_name_string(self):
        return ", ".join(self.common_names)

    def __str__(self):
        return self.common_names[0] or self.scientific_name

class Result(models.Model):
    fish_id = models.ForeignKey(to=Fish, on_delete=models.CASCADE)