from django.urls import path
from .views import EmployeView
from . import views

urlpatterns = [
    path('employes', EmployeView.as_view())
]
