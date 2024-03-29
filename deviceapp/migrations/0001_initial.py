# Generated by Django 3.2.3 on 2021-05-31 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LogUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logTitle', models.CharField(max_length=100)),
                ('LogUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logTitle', models.CharField(max_length=100)),
                ('LogDevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deviceapp.device')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='deviceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deviceapp.type'),
        ),
        migrations.AddField(
            model_name='device',
            name='deviceUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
