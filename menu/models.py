from django.db import models

# Create your models here.
from rest_framework import serializers


class Food(models.Model):

    name = models.CharField(max_length=60, null=True)
    price = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=60, null=True)


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'

