from tkinter import CASCADE
from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField()
    location = models.TextChoices()
    job_type = models.CharField(max_length=20)
    regimen_type = models.CharField(max_length=20)
    vacancies_count = models.IntegerField()
    subscribers_count = models.IntegerField()
    issued_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

    account = models.ManyToManyField(
        "accounts.Account", related_name="job_account"
    )

    skill = models.ManyToManyField(
        "skills.Skill", related_name="job_skill"
    )

    company = models.ForeignKey(
        "companies.Company", on_delete=CASCADE, related_name="job_company_id"
    )