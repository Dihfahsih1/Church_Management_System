# Generated by Django 3.0.6 on 2020-05-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0080_ministry_is_view_on_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]