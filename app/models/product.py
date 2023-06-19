from django.db import models

from app.models.base import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    product_code=models.CharField(max_length=50, unique=True,default='')
    amount_in_stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', related_name='products')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products",default='')

    class Meta:
        db_table = 'products'
