from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    # location = SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = [
            "id",
            "subscribers_count",
            "issued_at",
            "is_active",
            "company_id",
        ]

    # def get_location(self, address: Address) -> str:
    #     return Company.address.city
