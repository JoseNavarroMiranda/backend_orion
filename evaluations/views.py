from django.shortcuts import render
from rest_framework import generics
from .models import StackInfo
from .serializers import StackInfoSerializers

class StackInfoCreateAPIView(generics.CreateAPIView):
    queryset = StackInfo.objects.all()
    serializer_class = StackInfoSerializers

