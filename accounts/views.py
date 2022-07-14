from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status
from accounts.mixins import SerializerByMethodMixin
from accounts.permissions import (
    IsCandidateOnly,
    IsOwnerAccountOnly,
    IsAdmOnly,
    IsOwnerOrAdmin,
)
from rest_framework.authentication import TokenAuthentication


from .models import Account
from educations.models import Education
from educations.serializers import EducationSerializer, ListEducationSerializer
from . import serializers


# POST /api/accounts/register/ - registra um usuário.
class RegisterAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer


# GET /api/accounts/ - lista todos os usuários, somente admin.
class ListAccountsView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmOnly]

    queryset = Account.objects.all()
    serializer_class = serializers.ListAccountsSerializer


# POST /api/accounts/login/ - inicia sessão do usuário.
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


# GET /api/accounts/<int:pk>/ - recupera os dados do usuário, somente dono da conta.
# PATCH  /api/accounts/<int:pk>/ - atualiza parcialmente os dados do usuário, somente dono da conta.
# DELETE /api/accounts/<int:pk>/ - desativa a conta de um usuário, somente dono da conta.


class AccountsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer


# GET /api/accounts/<int:pk>/jobs/ - lista todas as vagas nas quais o candidato se inscreveu, somente dono da conta.
class ListJobsRegistredView(generics.ListAPIView):
    ...


# PATCH  /api/accounts/<int:pk>/company/<int:pk>/bind - associa um usuário recrutador a uma empresa, somente usuários recrutadores.
class AddCompanyToRecruiterView(generics.UpdateAPIView):
    ...


# PATCH /api/accounts/<str:email>/recover/ - reativa a conta de um usuário desativado, livre.
class ActiveAccountView(generics.UpdateAPIView):
    ...


# PATCH /api/accounts/<pk:int>/management/activation/ - ativa/desativa conta do usuário, somente admin.
class ActiveDeactiveAccountView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmOnly]

    queryset = Account.objects.all()
    serializer_class = serializers.ActiveDeactiveAccountSerializer


# Education Views


class ListCreateEducationsView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    permission_classes = [IsCandidateOnly]

    serializer_map = {
        "GET": ListEducationSerializer,
        "POST": EducationSerializer,
    }

    def perform_create(self, serializer):
        return serializer.save(account=self.request.user)


# List, Patch, Delete Educations From Education_Id


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


# List Educations From User Id


class ListEducationsAccount(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = ListEducationSerializer

    def get_queryset(self):
        account = get_object_or_404(Account, pk=self.kwargs["account_id"])

        return Education.objects.filter(account=account)
