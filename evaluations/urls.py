from django.urls import path
from .views import StackInfoCreateAPIView

app_name = "evaluations"

urlpatterns = [
    path("stack_info/", StackInfoCreateAPIView.as_view(), name = "stackinfo")
]