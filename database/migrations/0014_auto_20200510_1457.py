# Generated by Django 2.2.10 on 2020-05-10 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_auto_20200510_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='tanggal_post',
            new_name='tanggal',
        ),
    ]
