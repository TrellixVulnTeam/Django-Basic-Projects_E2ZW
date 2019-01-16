from django.db import models


class Name(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)


class Student(models.Model):
	name = models.ManyToManyField(Name)
	fathers_name = models.CharField(max_length=100)
	mothers_name = models.CharField(max_length=100)
