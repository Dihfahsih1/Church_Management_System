# Generated by Django 2.2.8 on 2020-02-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20200212_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Activity_Type',
            field=models.CharField(choices=[('Events', 'Events'), ('Church_Program', 'Church_Program')], default='----------', max_length=20),
        ),
    ]
