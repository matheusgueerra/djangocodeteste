from django import forms
from .models import Employee
from .models import Departament

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fieds = '__all__'


class DepartamentForm(forms.ModelForm):
    class Meta:
        model = Departament
        fields = '__all__'
