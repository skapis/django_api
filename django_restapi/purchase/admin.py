from django.contrib import admin
from .models import Purchase


class PurchaseDetail(admin.ModelAdmin):
    list_display = ['product', 'purchase_id', 'user']


admin.site.register(Purchase, PurchaseDetail)

