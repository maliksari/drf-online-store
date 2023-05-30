from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('client', 'Client')
    )

    role = models.CharField(max_length=6, choices=ROLES)
