# Generated by Django 2.2.8 on 2020-02-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0063_auto_20200221_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenues',
            name='Other_Notes',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
