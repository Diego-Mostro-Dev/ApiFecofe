# Generated by Django 4.1.6 on 2025-01-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiRestF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
