# Generated by Django 3.1.2 on 2020-10-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_type',
            field=models.CharField(choices=[('', 'Select Route Type'), ('one_way', 'One Way'), ('round_trip', 'Round Trip')], max_length=254),
        ),
    ]
