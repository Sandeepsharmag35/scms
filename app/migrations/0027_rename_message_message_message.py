# Generated by Django 5.0.1 on 2024-02-21 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Message',
            new_name='message',
        ),
    ]
