# Generated by Django 2.2.8 on 2020-01-24 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0079_auto_20200124_1155'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='customUsers',
            new_name='User',
        ),
    ]