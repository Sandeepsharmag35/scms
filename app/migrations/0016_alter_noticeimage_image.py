# Generated by Django 5.0.1 on 2024-01-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_notice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='notices/'),
        ),
    ]
