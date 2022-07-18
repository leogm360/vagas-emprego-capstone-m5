from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from companies.serializers import CompanyJobSerializer

from jobs.models import Job

class JobSerializer(serializers.ModelSerializer):
    location = SerializerMethodField()
    subscribers_count = SerializerMethodField()
    company = CompanyJobSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ["id", "title", "description", "salary", "location",  "job_type", "regimen_type", "vacancies_count", "subscribers_count", "issued_at", "company", "account"]
        read_only_fields = [
            "id",
            "issued_at",
            "is_active",
        ]
        extra_kwargs = {"account": {"write_only": True}}

    def get_location(self, job: Job) -> str:
        return job.company.address.city

    def get_subscribers_count(self, job:Job):
        accounts = job.account.all()
        subscribers_count = len(accounts)
        return subscribers_count

    def update(self, instance, validated_data):
        list_accounts = instance.account.all()
        account_data = validated_data.get('account')

        if(account_data not in list_accounts):
            instance.account.add(account_data)
        else:
            raise serializers.ValidationError({"detail": "You do not register again."})
        
        instance.save()
        return instance

class JobCreateSerializer(serializers.ModelSerializer):
    location = SerializerMethodField()
    subscribers_count = SerializerMethodField()
    company = CompanyJobSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ["id", "title", "description", "salary", "location",  "job_type", "regimen_type", "vacancies_count", "subscribers_count", "issued_at", "company"]
        read_only_fields = [
            "id",
            "issued_at",
            "is_active",
        ]

    def get_location(self, job: Job) -> str:
        return job.company.address.city

    def get_subscribers_count(self, job:Job):
        accounts = job.account.all()
        subscribers_count = len(accounts)
        return subscribers_count