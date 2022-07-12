from rest_framework import generics

from .models import Account
from .serializers import AccountSerializer

class RegisterAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ListAccountsView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
