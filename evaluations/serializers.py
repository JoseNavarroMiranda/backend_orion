from rest_framework import serializers
from .models import StackInfo

class StackInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = StackInfo
        fields = ("id", "name", "last_name", "email" ,"phone" , "description_service", "created_at")
        read_only_fields = ("id", "created_at")
