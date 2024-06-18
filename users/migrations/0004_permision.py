# Generated by Django 3.2.24 on 2024-06-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240318_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', models.CharField(max_length=60, null=True)),
                ('user_id', models.ManyToManyField(to='users.Employee')),
            ],
        ),
    ]