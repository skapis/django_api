from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserPurchaseSerializer, NewUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class UserList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({
            'users': {
                'total': users.count(),
                'items': serializer.data
            }
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserPurchases(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserPurchaseSerializer(users, many=True)
        return JsonResponse({
            'users': {
                'total': users.count(),
                'items': serializer.data
            }
        }, status=status.HTTP_200_OK)


class UserDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_user(self, request):
        try:
            user_id = request.GET.get('user', None)
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        user = self.get_user(request)
        data_range = request.GET.get('type', None)

        if data_range and data_range == 'full':
            serializer = UserPurchaseSerializer(user)
        else:
            serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


