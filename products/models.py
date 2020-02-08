from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.CharField(max_length=255)
    product_name=models.CharField(max_length=255)
    product_price=models.FloatField()
    image_url=models.CharField(max_length=2083)
