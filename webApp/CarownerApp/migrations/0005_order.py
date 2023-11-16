# Generated by Django 4.2.5 on 2023-09-25 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0008_carowner_rename_ownercar_customer_and_more'),
        ('CarownerApp', '0004_schedules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_customer_order', models.CharField(max_length=255, null=True)),
                ('name_driver_order', models.CharField(max_length=255, null=True)),
                ('name_schedule_order', models.CharField(max_length=255, null=True)),
                ('name_vehicle_order', models.CharField(max_length=255, null=True)),
                ('name_carowner_order', models.CharField(max_length=255, null=True)),
                ('carowner_id', models.IntegerField(null=True)),
                ('quantity_slot', models.IntegerField(null=True)),
                ('pickup_location', models.CharField(max_length=255, null=True)),
                ('dropoff_location', models.CharField(max_length=255, null=True)),
                ('pickup_datetime', models.DateTimeField(null=True)),
                ('dropoff_datetime', models.DateTimeField(null=True)),
                ('state_order', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LoginApp.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarownerApp.vehicle')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
