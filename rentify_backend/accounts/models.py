from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    USER_ROLE_CHOICES = [
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
    ]
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_role = models.CharField(max_length=50, choices=USER_ROLE_CHOICES)


   
    def __str__(self):
        return "{}".format(self.username)