# Generated by Django 5.0.1 on 2024-02-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_info_meta_description_info_meta_keywords_info_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='meta_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='gallery',
            name='meta_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='gallery',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]