from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    st_class = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student_table'
