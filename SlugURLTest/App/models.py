from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_status = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    product_slug_url =models.SlugField(max_length=3000)
