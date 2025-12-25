from rest_framework import serializers
from .models import StackInfo

class StackInfoSerializers(serializers.ModelSerializers):
    class Meta:
        model = StackInfo
        fields = ("id", "name", "lastname", "email" ,"phone" , "description_service", "created_at")
        read_only_fields = ("id", "created_at")
