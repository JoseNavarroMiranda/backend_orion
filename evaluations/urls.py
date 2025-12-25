from django.urls import path # type: ignore
from .views import StackInfoCreateAPIView

app_name = "evaluations"

urlpatterns = [
    path("stackinfo/", StackInfoCreateAPIView.as_view(), name = "stackinfo")
]