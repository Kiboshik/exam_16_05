from django.shortcuts import render
from rest_framework import response, views, status
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny

class UserRegisterAPIViews(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

