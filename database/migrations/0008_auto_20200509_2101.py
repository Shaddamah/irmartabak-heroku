# Generated by Django 2.2.10 on 2020-05-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20200509_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='martabak',
            name='highest_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]