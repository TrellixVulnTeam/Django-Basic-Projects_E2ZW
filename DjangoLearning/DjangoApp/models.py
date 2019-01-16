from django.db import models
from django.utils.text import slugify
from django.db.models import signals


class DjangoApp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    age = models.IntegerField()
    #slug = models.SlugField(unique=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "django_app"



#def yourmodel_pre_save(signal, instance, sender, **kwargs):
    #if not instance.slug:
       # slug = slugify(instance.first_name)  # change the attibute to the field that would be used as a slug
       # new_slug = slug,
        #count = 0
        #while DjangoApp.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
         #   count += 1
         #   new_slug = f'{slug}-{count}'

        #instance.slug = new_slug

# Execute signals pre_save
#signals.pre_save.connect(yourmodel_pre_save, sender=DjangoApp)
