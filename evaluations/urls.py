from django.urls import path # type: ignore
from .views import StackInfoCreateAPIView, CollaboratorListAPIView

app_name = "evaluations"

urlpatterns = [
    path("stackinfo/", StackInfoCreateAPIView.as_view(), name = "stackinfo"),
    path("collaborator/", CollaboratorListAPIView.as_view(), name = "collaborator"),
]