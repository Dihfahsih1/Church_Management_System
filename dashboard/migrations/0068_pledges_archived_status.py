# Generated by Django 2.2.8 on 2020-03-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0067_auto_20200227_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledges',
            name='Archived_Status',
            field=models.CharField(blank=True, choices=[('ARCHIVED', 'ARCHIVED'), ('NOT-ARCHIVED', 'NOT-ARCHIVED')], default='NOT-ARCHIVED', max_length=100, null=True),
        ),
    ]
