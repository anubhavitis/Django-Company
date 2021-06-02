# Generated by Django 3.2.3 on 2021-05-31 12:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deviceapp', '0005_auto_20210531_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='deviceMessage',
            field=models.CharField(default='New Device added.', max_length=100),
        ),
        migrations.AlterField(
            model_name='device',
            name='deviceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='deviceapp.type'),
        ),
        migrations.AlterField(
            model_name='logdevice',
            name='LogTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 12, 35, 22, 557950)),
        ),
        migrations.AlterField(
            model_name='loguser',
            name='LogTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 12, 35, 22, 558266)),
        ),
    ]
