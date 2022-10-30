from django.shortcuts import render
from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


class PurchaseList(APIView):
    def get(self, request):
        purchases = Purchase.objects.all()

        # Date filters
        from_date = request.GET.get('from', None)
        to_date = request.GET.get('to', None)

        if from_date and to_date:
            purchases = purchases.filter(purchase_date__range=[from_date, to_date])

        # Currency filter
        currency = request.GET.get('currency', None)

        if currency:
            purchases = purchases.filter(currency=currency)

        # Amount filter
        amount_from = request.GET.get('amount_from', None)
        amount_to = request.GET.get('amount_to', None)

        if amount_from and amount_to:
            purchases = purchases.filter(amount__lte=amount_to, amount__gte=amount_from)

        serializer = PurchaseSerializer(purchases, many=True)
        return Response({
            'purchases': {
                'total': purchases.count(),
                'items': serializer.data
            }
        }, status=status.HTTP_200_OK)

    def post(self, request):
        user_id = request.GET.get('user', None)
        if user_id:
            data = request.data
            data.update({'user': user_id})
            serializer = PurchaseSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        return Response({'result': 'user id is required'}, status=status.HTTP_400_BAD_REQUEST)


class PurchaseDetail(APIView):
    def get_purchase(self, request):
        try:
            id = request.GET.get('purchase', None)
            return Purchase.objects.get(purchase_id=id)
        except Purchase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        purchase = self.get_purchase(request)
        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        purchase = self.get_purchase(request)
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        purchase = self.get_purchase(request)
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

