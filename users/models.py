from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100, null=True)


class Permision(models.Model):

    user_id = models.ManyToManyField(Employee)
    permissions = models.CharField(max_length=60, null=True)
