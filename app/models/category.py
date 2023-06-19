from django.db import models

from app.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50,blank=False,null=False)
    category_code =models.CharField(max_length=50, unique=True,default='')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products",default='')

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name
