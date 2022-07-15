from django.shortcuts import get_object_or_404
from rest_framework import generics
from accounts.mixins import SerializerByMethodMixin
from accounts.permissions import IsRecruiterOnly, IsRecruiterOwnerOnly

from jobs.serializers import JobSerializer

from .models import Company

from .serializers import CompanySerializer
from addresses.models import Address
from addresses.serializers import AddressSerializer
from .permissions import CompaniesCustomPermissions, IsRecruiterOrAdmin


from jobs.models import Job
# from jobs.serializers import JobSerializer

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


# Jobs View

class ListJobView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class CreateJobView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    permission_classes = [IsRecruiterOnly]

    def perform_create(self, serializer):
        company_id = "a8440fba-bde7-4613-ae5f-1ea34960edda"
        company = Company.objects.get(id=company_id)
        print(company.__dict__)
        serializer.save(company=company)

class DetailJobView(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    permission_classes = [IsRecruiterOwnerOnly]

