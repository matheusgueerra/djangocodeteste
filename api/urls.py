from django.urls import path
from .views import Employe, deleteEmp
from . import views

urlpatterns = [
    path('employes', views.Employe),
    path('delete/<str:name', views.deleteEmp)
]
