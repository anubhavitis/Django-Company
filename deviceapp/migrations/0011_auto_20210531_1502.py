# Generated by Django 3.2.3 on 2021-05-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deviceapp', '0010_alter_logdevice_logtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logdevice',
            name='LogTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='loguser',
            name='LogTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]