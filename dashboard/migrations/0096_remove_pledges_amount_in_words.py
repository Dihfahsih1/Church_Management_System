# Generated by Django 2.2.8 on 2020-01-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0095_pledgescashedout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledges',
            name='Amount_In_Words',
        ),
    ]