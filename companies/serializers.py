from rest_framework import serializers
from .models import Company
from addresses.serializers import AddressSerializer

class CompanySerializer(serializers.ModelSerializer):
    adress = AddressSerializer()
    class Meta:
        model = Company
        fiedls = "__all__"