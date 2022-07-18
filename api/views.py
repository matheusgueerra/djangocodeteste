from email.policy import HTTP
from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from .models import Employee, Departament
from rest_framework import generics
from .serializers import EmployeeSerializer, DepartamentSerializer

from django.http import HttpResponse

# Create your views here.

def Employe(request):
    if request.method == "POST":

        form = Employee(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = Employee()
    return render(request, "addemp.html", {'form':form})

def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=name)
    employee.delete()
    return redirect("/showemp")

