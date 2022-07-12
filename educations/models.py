from django.db import models
from django.forms import CharField, DateField, DateTimeField

# Create your models here.

class Education(models.Model):
    institution_name = models.CharField(max_length=255)
    course = models.CharField(max_length=20)
    start_date = DateField()
    end_date = DateField()
    certificate_link = CharField(max_length=255)

    account = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="account_id", default=None)