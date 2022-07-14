from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from accounts.serializers import AccountSerializer

from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    # location = SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = ["id", "title", "description", "salary", "location",  "job_type", "regimen_type", "vacancies_count", "subscribers_count", "issued_at"]
        read_only_fields = [
            "id",
            "subscribers_count",
            "issued_at",
            "is_active",
            "company_id",
        ]

    # def get_location(self, address: Address) -> str:
    #     return Company.address.city

class UserRegisterJobSerializer(serializers.ModelSerializer):
    #account = AccountSerializer(read_only = True)

    class Meta:
        model = Job
        fields = ["id", "title", "description", "salary", "location",  "job_type", "regimen_type", "vacancies_count", "subscribers_count", "issued_at"]
        read_only_fields =["id", "title", "description", "salary", "location",  "job_type", "regimen_type", "vacancies_count", "subscribers_count", "issued_at"]

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)