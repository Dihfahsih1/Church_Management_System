# Generated by Django 2.2.8 on 2020-02-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_auto_20200213_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='mission_description',
            field=models.TextField(max_length=100000000),
        ),
        migrations.AlterField(
            model_name='about',
            name='vision_description',
            field=models.TextField(max_length=10000000),
        ),
    ]
