from rest_framework import serializers
from .models import Employee, Departament

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'departament')


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('numbers_of_employes')