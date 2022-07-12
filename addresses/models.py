from django.db import models

# Create your models here.


class Address(models.Model):
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    complement = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=20)
