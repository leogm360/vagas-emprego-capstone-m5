from addresses.serializers import AddressSerializer
from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Company
        fields ="__all__"
