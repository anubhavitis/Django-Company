# Generated by Django 3.2.3 on 2021-06-02 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deviceapp', '0013_auto_20210601_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='deviceUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device', to=settings.AUTH_USER_MODEL),
        ),
    ]
