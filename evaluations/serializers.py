from rest_framework import serializers
from .models import StackInfo, Collaborator


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ("id", "name", "last_name", "status", "role", "description", "image_field", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

class StackInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = StackInfo
        fields = ("id", "name", "last_name", "email" ,"phone" , "description_service", "created_at")
        read_only_fields = ("id", "created_at")
