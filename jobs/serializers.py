from asyncore import write
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from accounts.serializers import AccountSerializer

from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    # location = SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = ["id", "title", "description", "salary", "location",  "job_type", "regimen_type", "vacancies_count", "subscribers_count", "issued_at", "company_id"]
        read_only_fields = [
            "id",
            "subscribers_count",
            "issued_at",
            "is_active",
            "account"
        ]

    # def get_location(self, address: Address) -> str:
    #     return Company.address.city

class UserRegisterJobSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ["id", "title", "description", "salary", "location",  "job_type", "regimen_type", "vacancies_count", "subscribers_count", "issued_at","account"]
        read_only_fields =["id", "title", "description", "salary", "location",  "job_type", "regimen_type", "vacancies_count", "subscribers_count", "issued_at"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.location = validated_data.get('location', instance.location)
        instance.job_type = validated_data.get('job_type', instance.job_type)
        instance.regimen_type = validated_data.get('regimen_type', instance.regimen_type)
        instance.vacancies_count = validated_data.get('salary', instance.vacancies_count)
        instance.subscribers_count = validated_data.get('subscribers_count', instance.subscribers_count)
        instance.issued_at = validated_data.get('issued_at', instance.issued_at)

        instance.account = validated_data.get('account', instance.account)

        # account = []
        # for element in instance.account:
        #     if(element != self.account):
        #         account.append(element)

        # instance.account.set(account)

        # instance.save()
        # return instance




