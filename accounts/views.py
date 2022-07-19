from addresses.serializers import AddressSerializer
from companies.models import Company
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from educations.models import Education
from educations.serializers import EducationSerializer, ListEducationSerializer
from jobs.models import Job
from jobs.serializers import JobCreateSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status

from accounts.mixins import (
    SerializerByAccountTypeMixin,
    SerializerByMethodMixin,
)
from accounts.permissions import (
    IsAdmOnly,
    IsCandidateOnly,
    IsOwnerAccountOnly,
    IsOwnerOrAdmin,
)

from . import serializers
from .models import Account


class RegisterAccountView(SerializerByAccountTypeMixin, generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_map = {
        "CANDIDATE": serializers.AccountSerializer,
        "HUMAN_RESOURCES": serializers.AccountSerializerIsRH,
    }

    def create_address(self):
        address_data = self.request.data.get("address")

        serializer = AddressSerializer(data=address_data)

        serializer.is_valid()

        serializer.save()

        return serializer.instance

    def perform_for_candidate(self, address, serializer):
        serializer.save(address=address)

    def perform_for_human_resources(self, address, serializer):
        company_id = self.request.data.get("company_id")

        company = get_object_or_404(Company, pk=company_id)

        serializer.save(address=address, company=company)

    def perform_create(self, serializer):
        address = self.create_address()

        is_human_resources = self.request.data.get("is_human_resources", False)

        if is_human_resources:
            self.perform_for_human_resources(address, serializer)
        else:
            self.perform_for_candidate(address, serializer)


class ListAccountsView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmOnly]

    queryset = Account.objects.all()
    serializer_class = serializers.ListAccountsSerializer


class LoginAccountsView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"},
            status.HTTP_401_UNAUTHORIZED,
        )


class AccountsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = Account.objects.all()
    serializer_class = serializers.ListAccountsSerializer


class ListJobsRegistredView(generics.ListAPIView):
    ...


class AddCompanyToRecruiterView(generics.UpdateAPIView):
    ...


class ActiveAccountView(generics.UpdateAPIView):
    ...


class ActiveDeactiveAccountView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmOnly]

    queryset = Account.objects.all()
    serializer_class = serializers.ActiveDeactiveAccountSerializer


class ListCreateEducationsView(
    SerializerByMethodMixin, generics.ListCreateAPIView
):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    permission_classes = [IsCandidateOnly]

    serializer_map = {
        "GET": ListEducationSerializer,
        "POST": EducationSerializer,
    }

    def perform_create(self, serializer):
        return serializer.save(account=self.request.user)


class RetrievePatchEducationView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    permission_classes = [IsOwnerAccountOnly]

    serializer_map = {
        "GET": ListEducationSerializer,
        "PATCH": ListEducationSerializer,
    }


class ListEducationsAccount(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = ListEducationSerializer

    def get_queryset(self):
        account = get_object_or_404(Account, pk=self.kwargs["account_id"])

        return Education.objects.filter(account=account)


class UserRegisterJobView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer

    lookup_url_kwarg = "job_id"

    permission_classes = [IsCandidateOnly]

    def perform_update(self, serializer):
        serializer.save(account=self.request.user)
