# Generated by Django 2.2.8 on 2020-02-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0047_auto_20200218_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingrenovation',
            name='archivedmonth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buildingrenovation',
            name='archivedyear',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
