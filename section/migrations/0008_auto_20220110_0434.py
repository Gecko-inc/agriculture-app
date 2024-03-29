# Generated by Django 3.1.6 on 2022-01-10 01:34

import config.core
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0007_auto_20220110_0317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date', '-id'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='license',
            name='image',
            field=models.ImageField(upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='license',
            name='image_de',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='license',
            name='image_en',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='license',
            name='image_ru',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
    ]
