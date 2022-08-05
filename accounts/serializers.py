

from rest_framework import serializers

from accounts.models import Categories, Currency, Transaction


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class  Meta:
        model = Categories
        fields = '__all__'
        