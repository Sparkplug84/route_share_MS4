# Generated by Django 3.1.2 on 2020-10-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20201026_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6),
        ),
    ]