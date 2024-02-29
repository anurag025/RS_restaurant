from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_name = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=1000, null=True)
    doc = models.CharField(max_length=60, null=True)
