# Generated by Django 3.2.3 on 2021-05-31 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deviceapp', '0004_alter_device_deviceuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='logdevice',
            name='LogTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 10, 23, 9, 141323)),
        ),
        migrations.AddField(
            model_name='loguser',
            name='LogTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 10, 23, 9, 141636)),
        ),
    ]
