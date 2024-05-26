from django.db import models
from django.conf import settings
from accounts.models import User


class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    nearby_hospitals = models.TextField(max_length=1000)
    nearby_colleges = models.TextField(max_length=1000)
    description = models.TextField(max_length=2000, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.place} - {self.area} sqm'