from rest_framework import generics
from accounts.permissions import IsRecruiterOnly, IsRecruiterOwnerOnly

from jobs.serializers import JobSerializer

from .models import Company

from .serializers import CompanySerializer
from addresses.models import Address
from addresses.serializers import AddressSerializer
from .permissions import CompaniesCustomPermissions, IsRecruiterOrAdmin


from jobs.models import Job

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
    permission_classes = [CompaniesCustomPermissions]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_update(self, serializer):
        if "address" in self.request.data:
            addressserializer = AddressSerializer(data=self.request.data["address"])
            addressserializer.is_valid()
            ad1 = Address.objects.create(**addressserializer.validated_data)
            ad1.save()
            serializer.save(address=ad1)
        serializer.save()     


# Jobs View

class ListJobView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class CreateJobView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    permission_classes = [IsRecruiterOnly]

    def perform_create(self, serializer):
        company_id = self.request.user.company.id
        company = Company.objects.get(id=company_id)
        serializer.save(company=company)

class DetailJobView(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    permission_classes = [IsRecruiterOwnerOnly]

