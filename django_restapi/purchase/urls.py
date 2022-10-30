from django.urls import path, include
from .views import PurchaseList, PurchaseDetail

urlpatterns = [
    path('list', PurchaseList.as_view(), name='list'),
    path('detail', PurchaseDetail.as_view(), name='detail')
]
