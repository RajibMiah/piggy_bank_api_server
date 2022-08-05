from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from accounts.models import Categories, Currency, Transaction
from accounts.serializers import (CategorySerializer, CurrencySerializer,
                                  ReadOnlyTransactionSerializer,
                                  WriteOnlyTransactionSerializer)


class CurrencyListApiView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None

class CategoryModelViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    
class TransactionModelViewSet(ModelViewSet):

    queryset = Transaction.objects.select_related("currency" , "category")
    pagination_class = None

    #TODO:: serach filter not working    
    filter_backends = [filters.OrderingFilter , filters.SearchFilter]
    search_fields = ("description",)
    ordering_fields = ("amount" , "date")

    def get_serializer_class(self):
        if self.action in ('list' , 'retrieve'):
            return ReadOnlyTransactionSerializer
        return WriteOnlyTransactionSerializer     
