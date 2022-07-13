from django.conf import settings
from django.db import models

# Create your models here.

class Education(models.Model):
    institution_name = models.CharField(max_length=255)
    course = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    certificate_link = models.CharField(max_length=255)

    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="account_id", default=None)