# Generated by Django 3.1.6 on 2021-09-05 13:16

import config.views
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_auto_20210905_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='image',
            field=models.ImageField(blank=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
    ]
