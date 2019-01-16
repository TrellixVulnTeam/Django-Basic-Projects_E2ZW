from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_table'

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post_table'
