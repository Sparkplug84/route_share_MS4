# Generated by Django 3.1.2 on 2020-11-30 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20201020_1957'),
        ('profiles', '0004_auto_20201129_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='membership.membership'),
        ),
    ]
