# Generated by Django 5.0.1 on 2024-02-18 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_meta_description_event_meta_keywords_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='meta_keywords',
        ),
    ]