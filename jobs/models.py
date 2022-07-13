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
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=9, choices=JobChoices.choices)
    regimen_type = models.CharField(
        max_length=10, choices=RegimeChoices.choices
    )
    vacancies_count = models.IntegerField(validators=[MinValueValidator(1)])
    subscribers_count = models.IntegerField(default=0)
    issued_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    account = models.ManyToManyField(
        "accounts.Account", related_name="accounts_id"
    )

    # skill = models.ManyToManyField(
    #     "skills.Skill", related_name="skill_id"
    # )

    # company = models.ForeignKey(
    #     "companies.Company", on_delete=models.CASCADE, related_name="company_id"
    # )
