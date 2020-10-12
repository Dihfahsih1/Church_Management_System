# Generated by Django 2.2.8 on 2020-06-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0102_auto_20200609_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Archived_Status',
            field=models.CharField(blank=True, choices=[('ARCHIVED', 'ARCHIVED'), ('NOT-ARCHIVED', 'NOT-ARCHIVED')], default='NOT-ARCHIVED', max_length=1000, null=True),
        ),
    ]
