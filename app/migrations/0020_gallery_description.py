# Generated by Django 5.0.1 on 2024-02-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_gallery_galleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
