from django.db import models

class PasswordModel(models.Model):
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'PasswordModel'
