

from dataclasses import fields

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

class WriteOnlyTransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field="code" , queryset = Currency.objects.all())
    
    class Meta:
        model = Transaction
        fields = (
           
            "amount",
            "currency",
            "date",
            "description",
            "category",
        )      
        

class ReadOnlyTransactionSerializer(serializers.ModelSerializer):
    
    currency = CurrencySerializer()
    
    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "currency",
            "date",
            "description",
            "category",
        )
        read_only_fields = fields
