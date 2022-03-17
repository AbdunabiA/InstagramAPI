from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Account
from .serializers import AccountSerializer


class AccountListCreateApi(ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
class AccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

