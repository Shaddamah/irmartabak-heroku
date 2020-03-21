# Generated by Django 2.2.10 on 2020-03-21 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_remove_martabak_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='martabak',
            name='rating',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.STAR_RATINGS_RATING_MODEL),
        ),
    ]
