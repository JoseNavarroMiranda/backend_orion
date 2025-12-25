from django.shortcuts import render
from rest_framework import generics
from .models import StackInfo
from .serializers import StackInfo

class StackInfoCreateAPIView(generics.CreateAPIView):
    queryset = StackInfo.objects.all()
    serializers_class = StackInfoSerializers

