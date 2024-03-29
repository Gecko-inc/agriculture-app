# Generated by Django 3.1.6 on 2022-02-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20220110_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_de',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_ru',
        ),
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='product',
            name='file_de',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='product',
            name='file_en',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='product',
            name='file_ru',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл'),
        ),
    ]
