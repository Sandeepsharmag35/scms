# Generated by Django 5.0.1 on 2024-01-26 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_aboutusimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
    ]
