# Generated by Django 2.2.8 on 2020-01-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0066_auto_20200113_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='Reason_For_Payment',
            field=models.CharField(choices=[('Church Renovations', 'Church Renovations'), ('Water Bills', 'Water Bills'), ('YB', 'Yaka Bills'), ('Transport', 'Transport'), ('LO', 'Love Offering'), ('MB', 'Medical Bills'), ('Rent', 'Rent'), ('Help', 'Help'), ('Drinks', 'Drinks'), ('Savings', 'Savings'), ('Evangelism', 'Evangelism')], max_length=100),
        ),
        migrations.AlterField(
            model_name='sundryreportarchive',
            name='Reason',
            field=models.CharField(choices=[('Lunch', 'Lunch'), ('Upkeep', 'Upkeep')], max_length=100, null=True),
        ),
    ]