# Generated by Django 2.2.8 on 2020-10-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0128_auto_20201012_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='banner',
            field=models.ImageField(blank=True, max_length=10000, null=True, upload_to='about/'),
        ),
    ]