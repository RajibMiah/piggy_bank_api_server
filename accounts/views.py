from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from accounts.models import Categories, Currency, Transaction
from accounts.serializers import (CategorySerializer, CurrencySerializer,
                                  ReadOnlyTransactionSerializer,
                                  WriteOnlyTransactionSerializer)


class CurrencyListApiView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    
class TransactionModelViewSet(ModelViewSet):

    queryset = Transaction.objects.all()
    
    def get_serializer_class(self):
        if self.action in ('list' , 'retrieve'):
            return ReadOnlyTransactionSerializer
        return WriteOnlyTransactionSerializer     
