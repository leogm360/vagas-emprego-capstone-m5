import uuid

from django.db import models


class Company(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=11)
    date_joined = models.DateTimeField(auto_now=True)

    address = models.OneToOneField(
        "addresses.Address", on_delete=models.CASCADE
    )
