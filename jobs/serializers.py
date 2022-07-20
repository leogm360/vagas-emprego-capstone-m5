from companies.serializers import CompanyJobSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import (
    CharField,
    IntegerField,
    ListField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)
from skills.models import Skill

from jobs.models import Job


class JobBaseSerializer(ModelSerializer):
    subscribers_count = SerializerMethodField()
    company = CompanyJobSerializer(read_only=True)

    class Meta:
        model = Job
        depth = 1

    def get_subscribers_count(self, job: Job) -> int:
        return job.account.count()


class JobCreateSerializer(JobBaseSerializer):
    location = CharField(required=False)
    skills_id = ListField(
        child=IntegerField(min_value=0),
        allow_empty=False,
        write_only=True,
    )

    class Meta(JobBaseSerializer.Meta):
        exclude = ["account"]
        read_only_fields = [
            "issued_at",
            "is_active",
        ]

    def set_skills(self, job: Job, skills_data: dict) -> None:
        errors = {}

        for skill_id in skills_data:
            try:
                skill = Skill.objects.get(pk=skill_id)

                job.skills.add(skill)
            except ObjectDoesNotExist:
                if not errors.get("skills", False):
                    errors["skills"] = []

                errors["skills"].append(
                    f"Skill with id {skill_id} does not exist."
                )

        if errors.get("skills", False):
            raise ValidationError(errors)

    def create(self, validated_data: dict) -> Job:
        location_data = validated_data.pop("location", False)
        skills_data = validated_data.pop("skills_id")

        job: Job = Job.objects.create(**validated_data)

        if not location_data:
            job.location = job.company.address.city
        else:
            job.location = location_data

        self.set_skills(job, skills_data)

        job.save()

        return job

    def update(self, instance: Job, validated_data: dict) -> Job:
        skills_data = validated_data.pop("skills_id", False)
        account_data = validated_data.pop("account", False)

        job = super().update(instance, validated_data)

        if skills_data:
            self.set_skills(job, skills_data)

        if account_data:
            has_account = job.account.filter(email=account_data.email).exists()

            if has_account:
                raise ValidationError(
                    {
                        "job": f"User {account_data.first_name} {account_data.last_name} cannot apply multiple times."
                    }
                )
            else:
                job.account.add(account_data)

        job.save()

        return job


class JobSearchSerializer(JobBaseSerializer):
    class Meta(JobBaseSerializer.Meta):
        exclude = ["account"]
        read_only_fields = [
            "issued_at",
            "is_active",
        ]
