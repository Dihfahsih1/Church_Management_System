# Generated by Django 2.2.8 on 2020-10-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0126_auto_20201011_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(blank=True, default='slate-gray', max_length=40, null=True),
        ),
    ]
