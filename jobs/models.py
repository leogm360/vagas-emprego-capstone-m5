from django.core.validators import MinValueValidator
from django.db import models


class JobChoices(models.TextChoices):
    CLT = ("CLT",)
    PJ = ("PJ",)
    TEMPORARY = ("TEMPORARY",)


class RegimeChoices(models.TextChoices):
    PRESENCIAL = ("PRESENCIAL",)
    REMOTE = ("REMOTE",)
    HYBRID = ("HYBRID",)


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=5)
    location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=9, choices=JobChoices.choices)
    regimen_type = models.CharField(
        max_length=10, choices=RegimeChoices.choices
    )
    vacancies_count = models.IntegerField(validators=[MinValueValidator(1)])
    issued_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    account = models.ManyToManyField(
        "accounts.Account", related_name="accounts_id",
    )

    company = models.ForeignKey(
        "companies.Company", on_delete=models.CASCADE, related_name="company_id"
    )

    skills = models.ManyToManyField(
        "skills.Skill", related_name="skill_id"
    )

