# Generated by Django 4.2.5 on 2023-11-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarownerApp', '0002_orders_total_price_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='price_schedule',
            field=models.IntegerField(null=True),
        ),
    ]
