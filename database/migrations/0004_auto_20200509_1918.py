# Generated by Django 2.2.10 on 2020-05-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20200509_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='martabak',
            name='image',
            field=models.ImageField(upload_to='img/martabak/%y/%m/%d'),
        ),
    ]
