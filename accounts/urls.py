
from django.urls import path
from rest_framework import routers

from accounts.views import (CategoryModelViewSet, CurrencyListApiView,
                            TransactionModelViewSet)

router = routers.SimpleRouter()
router.register(f'categories' , CategoryModelViewSet , basename='category')
router.register(f'transaction' , TransactionModelViewSet , basename='transaction' )

urlpatterns = [
    path('currencies/' , CurrencyListApiView.as_view() , name ='currencies')
] + router.urls
