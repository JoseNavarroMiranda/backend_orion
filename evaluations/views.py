from django.shortcuts import render
from rest_framework import generics
from .models import StackInfo, Collaborator
from .serializers import StackInfoSerializers, CollaboratorSerializer

class StackInfoCreateAPIView(generics.CreateAPIView):
    queryset = StackInfo.objects.all()
    serializer_class = StackInfoSerializers

class CollaboratorListAPIView(generics.ListAPIView):
    queryset = Collaborator.objects.filter(status=True) #Filter to active collaborator
    serializer_class = CollaboratorSerializer