from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    # qo'shimcha fieldlar
    address = models.CharField(max_length=50)
    phone = PhoneNumberField(blank=True, unique=True)
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username