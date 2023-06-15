from django.db import models

from app.models.base import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    amount_in_stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', related_name='products')
    
