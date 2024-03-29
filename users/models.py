from django.db import models

# Create your models here.
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class Employee(models.Model):
    name = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100, null=True)


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    name = serializers.CharField(max_length=60)
    phone = serializers.CharField(max_length=10)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone']

    def create(self, validated_data):
        # Customize how Employee objects are created
        return Employee.objects.create(**validated_data)

    def validate_phone(self, value):
        if Employee.objects.filter(phone=value).exists():
            raise serializers.ValidationError(f'User with this phone number {value} already exist.')
        return value

