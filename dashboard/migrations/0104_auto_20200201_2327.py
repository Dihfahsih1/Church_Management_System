# Generated by Django 2.2.8 on 2020-02-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0103_auto_20200201_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledgeitem',
            name='Item_That_Needs_Pledges',
            field=models.CharField(default='Item', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
