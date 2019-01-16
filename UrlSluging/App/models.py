from django.db import models
from App.utils import unique_slug_generator
from django.db.models.signals import pre_save

class Student(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default='')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "student_table"


    def save(self, *args, **kwargs):
        if self.featured:
            qs = Student.objects.filter(featured=True).exclude(pk=self.pk)
            if qs.exists():
                qs.update(featured=False)
        super(Student, self).save(*args, **kwargs)


def pre_save_receiver_page_model(sender, instance, *args, **kwargs):
    if instance.slug == '':
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver_page_model, sender=Student)