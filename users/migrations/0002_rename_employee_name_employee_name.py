# Generated by Django 3.2.24 on 2024-03-15 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee_name',
            new_name='name',
        ),
    ]
