# Generated by Django 4.2.5 on 2023-10-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarownerApp', '0014_customsession_delete_carownersession_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsession',
            name='expire_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customsession',
            name='session_data',
            field=models.TextField(null=True),
        ),
    ]