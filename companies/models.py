from django.db import models
from django.utils import timezone
import uuid

class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name=models.CharField(max_length=255)
    cnpj=models.CharField(max_length=14) 
    phone=models.CharField(max_length=11)
    date_joined= models.DateTimeField(default=timezone.now())
    adress= models.OneToOneField("addresses.Adress",on_delete=models.CASCADE)
