from django.db import models

# Create your models here.
from rest_framework import serializers

class Employee(models.Model):
    employee_name = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
