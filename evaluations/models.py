from django.db import models

import uuid


STATUS_CHOICES = (
    (True, "Activo"),
    (False, "Inactivo"),
)

class Collaborator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)
    role = models.CharField(max_length=200)
    description = models.CharField(max_length=250, null=True, blank=True)
#    image_field = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StackInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    phone = models.IntegerField()
    description_service = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
