from django.db import models

from app.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name
