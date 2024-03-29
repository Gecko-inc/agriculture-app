# Generated by Django 3.1.6 on 2022-02-10 04:23

import config.core
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0008_auto_20220110_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_de',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_en',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_ru',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
    ]
