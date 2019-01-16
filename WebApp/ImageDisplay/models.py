from django.db import models





class Employee(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/')

    class Meta:
        db_table = 'db_employee'
