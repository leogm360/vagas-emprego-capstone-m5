from addresses.models import Adress
from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Company
from .serializers import CompanySerializer


class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        adress = get_object_or_404(Adress, zip_code=self.request.zip_code)
        serializer.save(adress=adress)
