from django.db import models


class Full_Name(models.Model):
	name_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='name_id')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)


class Full_Address(models.Model):
	address_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='address_id')
	address_country = models.CharField(max_length=100)
	address_city = models.CharField(max_length=100)
	address_village = models.CharField(max_length=100)
	address_zip = models.CharField(max_length=50)


class Student_Info(models.Model):
	student_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='student_id')
	student_name = models.ForeignKey(Full_Name, on_delete = models.CASCADE)
	student_age = models.IntegerField()
	student_address = models.ForeignKey(Full_Address, on_delete = models.CASCADE)