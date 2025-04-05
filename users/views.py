from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status

# Registration view using DRF's generic CreateAPIView
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

