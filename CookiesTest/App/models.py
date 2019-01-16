from django.db import models





class Student(models.Model):

    student_name = models.CharField(max_length=100)
    student_age = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = 'table_student'