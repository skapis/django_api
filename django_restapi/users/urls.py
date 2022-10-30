from django.urls import path, include
from .views import UserList, UserPurchases, UserDetail

urlpatterns = [
    path('list', UserList.as_view(), name='list'),
    path('purchases', UserPurchases.as_view(), name='user_purchase'),
    path('detail', UserDetail.as_view(), name='user_detail')
]
