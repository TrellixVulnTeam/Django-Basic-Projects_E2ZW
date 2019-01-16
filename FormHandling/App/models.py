from django.db import models


class StudentModel(models.Model):
    title = models.CharField(max_length=100)