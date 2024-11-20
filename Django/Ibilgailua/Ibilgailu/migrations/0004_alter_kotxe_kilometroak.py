# Generated by Django 5.1.1 on 2024-10-12 16:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ibilgailu', '0003_remove_kotxe_alokatzailea_remove_kotxe_alokatze_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kotxe',
            name='kilometroak',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]