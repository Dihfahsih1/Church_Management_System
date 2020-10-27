# Generated by Django 2.2.8 on 2020-10-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_revenues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenues',
            name='Electricity_Amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='revenues',
            name='General_Offering_Amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='revenues',
            name='Seed_Amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='revenues',
            name='Tithe_Amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
