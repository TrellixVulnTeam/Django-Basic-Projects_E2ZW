from django.db import models


class Garden(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default='')


class Flower(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=100)
    description = models.TextField(default='')
    garden = models.ForeignKey(Garden, null=True, default=None, on_delete=models.CASCADE)
