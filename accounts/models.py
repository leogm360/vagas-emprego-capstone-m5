from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import CustomUserManager


class GenderFieldChoice(models.TextChoices):
    male = ("Male",)
    female = ("Female",)
    male_transgender = ("Male Transgender",)
    female_transgender = ("Female Transgender",)
    non_binary = ("Non Binary",)
    other = ("Other",)


class Account(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    gender = models.CharField(
        max_length=50,
        choices=GenderFieldChoice.choices,
    )
    phone = models.CharField(max_length=11, unique=True)
    is_human_resources = models.BooleanField(default=False)

    address = models.OneToOneField("addresses.Address", on_delete=models.CASCADE, null=True)

    company = models.ForeignKey(
    "companies.Company", on_delete=models.CASCADE, related_name="accounts", null=True
    )

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "cpf",
        "gender",
        "phone",
    ]
    objects = CustomUserManager()
