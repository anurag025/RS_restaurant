from django.contrib import admin

# Register your models here.
from .models import Employee, Permision

admin.site.register(Employee)
admin.site.register(Permision)

