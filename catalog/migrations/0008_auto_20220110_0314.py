# Generated by Django 3.1.6 on 2022-01-10 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20220109_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'ordering': ['-date', '-id'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]