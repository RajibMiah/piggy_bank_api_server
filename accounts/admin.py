from django.contrib import admin

from .models import Categories, Currency, Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categories)
admin.site.register(Currency)
