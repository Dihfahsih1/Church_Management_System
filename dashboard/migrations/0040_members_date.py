# Generated by Django 2.2.8 on 2020-02-17 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_auto_20200217_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]