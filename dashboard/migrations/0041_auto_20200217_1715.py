# Generated by Django 2.2.8 on 2020-02-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0040_members_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
