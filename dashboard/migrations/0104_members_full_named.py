# Generated by Django 2.2.8 on 2020-06-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0103_members_archived_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Full_Named',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]