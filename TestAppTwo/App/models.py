from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)