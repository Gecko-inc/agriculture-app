# Generated by Django 3.1.6 on 2022-02-11 18:44

import config.core
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_productreview_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmedia',
            name='iframe',
        ),
        migrations.RemoveField(
            model_name='productmedia',
            name='iframe_de',
        ),
        migrations.RemoveField(
            model_name='productmedia',
            name='iframe_en',
        ),
        migrations.RemoveField(
            model_name='productmedia',
            name='iframe_ru',
        ),
        migrations.AddField(
            model_name='product',
            name='iframe',
            field=models.TextField(blank=True, verbose_name='Видео с YouTube'),
        ),
        migrations.AlterField(
            model_name='productmedia',
            name='image',
            field=models.ImageField(upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='productmedia',
            name='image_de',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='productmedia',
            name='image_en',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='productmedia',
            name='image_ru',
            field=models.ImageField(null=True, upload_to=config.core.get_upload_to, verbose_name='Изображение'),
        ),
    ]