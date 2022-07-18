from email.policy import HTTP
from http.client import HTTPResponse
from django.shortcuts import render
from .models import Employee, Departament
from rest_framework import generics
from .serializers import EmployeeSerializer, DepartamentSerializer
from django.http import HttpResponse

# Create your views here.

class EmployeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class DepartamentView(generics.ListAPIView):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer


