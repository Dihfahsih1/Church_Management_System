# Generated by Django 2.2.8 on 2020-02-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0042_auto_20200218_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Secretary', 'Secretary'), ('SuperAdmin', 'SuperAdmin'), ('Building Chair', 'Building Chair'), ('Marrieds Leader', 'Marrieds Leader'), ('Youth Leader', 'Youth Leader'), ('Ordinary', 'Ordinary'), ('Website Admin', 'Website Admin')], max_length=250),
        ),
    ]
