# Generated by Django 2.2.17 on 2021-03-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210302_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]