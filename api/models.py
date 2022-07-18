import email
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    departament = models.CharField(max_length=150)


class Departament(models.Model):
    numbers_of_employes = models.IntegerField()

