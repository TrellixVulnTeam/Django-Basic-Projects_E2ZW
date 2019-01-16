from django.db import models



class Cars(models.Model):
	user_id = models.AutoField(primary_key=True)
	car_model = models.CharField(max_length=50)


class Person(models.Model):
	car_name = models.ForeignKey(Cars, on_delete = models.CASCADE)