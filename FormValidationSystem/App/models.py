from django.db import models

class Employee(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100, unique=True)
    user_password = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=100)
    user_qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "emp_table"
