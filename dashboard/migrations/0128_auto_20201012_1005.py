# Generated by Django 2.2.8 on 2020-10-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0127_auto_20201012_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='is_active',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10),
        ),
    ]
