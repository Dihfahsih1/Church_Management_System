# Generated by Django 2.2.8 on 2020-06-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0088_auto_20200603_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=models.TextField(max_length=100000),
        ),
    ]
