from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "Emaployee"
