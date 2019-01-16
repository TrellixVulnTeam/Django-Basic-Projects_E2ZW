from django.db import models

class PasswordReset(models.Model):
    res_pass = models.CharField(max_length=8)
