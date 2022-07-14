from rest_framework import generics

from accounts.permissions import IsCandidateOnly, IsRecruiterOnly
from .models import Company 
from .serializers import CompanySerializer
from addresses.models import Address 
from addresses.serializers import AddressSerializer
from .permissions import CompaniesCustomPermissions

from jobs.models import Job
from jobs.serializers import JobSerializer

class CompanyView(generics.ListCreateAPIView):
    permission_classes = [CompaniesCustomPermissions]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        addressserializer=AddressSerializer(data=self.request.data["address"])
        addressserializer.is_valid()
        ad1 = Address.objects.create(**addressserializer.validated_data)
        ad1.save()
        serializer.save(address=ad1)


class DetailCompanyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CompaniesCustomPermissions]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_update(self, serializer):
        addressserializer=AddressSerializer(data=self.request.data["address"])
        addressserializer.is_valid()
        ad1 = Address.objects.create(**addressserializer.validated_data)
        ad1.save()
        serializer.save(address=ad1)


#Jobs views

class CreateJobView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    permission_classes = [IsRecruiterOnly]

    def perform_create(self, serializer):
        company = Company.objects.get(id=self.request.user.company_id)

        serializer(data=self.request, company=company)


class ListJobView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class DetailJobView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
        




    
    

