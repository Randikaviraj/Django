from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list=('product_name')


    
admin.site.register(Product,ProductAdmin)


