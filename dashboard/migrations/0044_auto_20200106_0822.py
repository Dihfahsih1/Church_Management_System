# Generated by Django 2.2.8 on 2020-01-06 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0043_auto_20200103_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerings',
            name='AmountInWords',
        ),
        migrations.RemoveField(
            model_name='offerings',
            name='DayOfTheWeek',
        ),
    ]