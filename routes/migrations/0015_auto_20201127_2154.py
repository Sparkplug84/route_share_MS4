# Generated by Django 3.1.2 on 2020-11-27 21:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('routes', '0014_route_save_routes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='save_routes',
        ),
        migrations.AddField(
            model_name='route',
            name='save',
            field=models.ManyToManyField(blank=True, related_name='save', to=settings.AUTH_USER_MODEL),
        ),
    ]
