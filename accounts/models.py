from tabnanny import verbose

from django.db import models


# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3 , unique=True)
    name = models.CharField(max_length=32, blank=True , null = True)

    class Meta:
        verbose_name = 'Currencie'

    def __str__(self) -> str:
        return str(self.code)

class Categories(models.Model):
    name = models.CharField(max_length=32 , blank=True)
    
    class Meta:
        verbose_name = 'Categorie'
    
    def __str__(self) -> str:
        return self.name

class Transaction(models.Model):
    amonut = models.DecimalField(max_digits=32 , decimal_places=2)
    currency = models.ForeignKey(Currency , on_delete=models.PROTECT , related_name='transactions')
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(Categories , on_delete=models.SET_NULL , null= True, blank = True,  related_name='transactions') 
    
    class Meta:
        verbose_name = 'Transaction'

    def __str__(self) -> str:
        return f"{self.amonut} {self.currency.code} {self.date}"
