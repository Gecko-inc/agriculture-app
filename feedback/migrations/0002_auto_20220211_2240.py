# Generated by Django 3.1.6 on 2022-02-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='phone',
            field=models.CharField(default=' ', max_length=210, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='surname',
            field=models.CharField(default=' ', max_length=210, verbose_name='Фамилия'),
        ),
    ]
