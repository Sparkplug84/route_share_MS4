# Generated by Django 3.1.2 on 2020-11-06 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20201026_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
