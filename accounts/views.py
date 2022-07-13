from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status

from .models import Account
from .serializers import AccountSerializer, LoginSerializer


# POST /api/accounts/register/ - registra um usuário.
class RegisterAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# GET /api/accounts/ - lista todos os usuários, somente admin.
class ListAccountsView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# POST /api/accounts/login/ - inicia sessão do usuário.
class LoginAccountsView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
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

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# GET /api/accounts/<int:pk>/jobs/ - lista todas as vagas nas quais o candidato se inscreveu, somente dono da conta.


# PATCH  /api/accounts/<int:pk>/company/<int:pk>/bind - associa um usuário recrutador a uma empresa, somente usuários recrutadores.


# PATCH /api/accounts/<str:email>/recover/ - reativa a conta de um usuário desativado, livre.


# PATCH /api/accounts/<pk:int>/management/activation/ - ativa/desativa conta do usuário, somente admin.
