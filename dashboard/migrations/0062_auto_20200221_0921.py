# Generated by Django 2.2.8 on 2020-02-21 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0061_auto_20200220_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allowance',
            name='Name',
        ),
        migrations.DeleteModel(
            name='AllowanceReportArchive',
        ),
        migrations.DeleteModel(
            name='Allowance',
        ),
    ]
