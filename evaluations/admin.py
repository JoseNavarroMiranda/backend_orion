from django.contrib import admin
from .models import Collaborator, StackInfo

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "role", "status")
    list_filter = ("status", "role")
    search_fields = ("name", "last_name", "role")
    ordering = ("last_name", "name")


@admin.register(StackInfo)
class StackInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "description_service", "created_at")
    readonly_fields = ("email", "phone", "description_service", "created_at")
    search_fields = ("email",)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False