# Generated by Django 3.1.2 on 2020-11-12 21:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0009_auto_20201112_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='length',
            field=models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(5)]),
        ),
    ]
