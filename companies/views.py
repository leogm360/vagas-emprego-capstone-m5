from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Company

from .serializers import CompanySerializer
from addresses.models import Address
from addresses.serializers import AddressSerializer
from .permissions import CompaniesCustomPermissions, IsRecruiterOrAdmin


from jobs.models import Job
from jobs.serializers import JobSerializer

class CompanyView(generics.ListCreateAPIView):
    permission_classes = [CompaniesCustomPermissions]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        addressserializer = AddressSerializer(data=self.request.data["address"])
        addressserializer.is_valid()
        ad1 = Address.objects.create(**addressserializer.validated_data)
        ad1.save()
        serializer.save(address=ad1)


class DetailCompanyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsRecruiterOrAdmin]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_update(self, serializer):
        addressserializer = AddressSerializer(data=self.request.data["address"])
        addressserializer.is_valid()
        ad1 = Address.objects.create(**addressserializer.validated_data)
        ad1.save()
        serializer.save(address=ad1)
