# Generated by Django 3.1.6 on 2022-02-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20220210_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
    ]