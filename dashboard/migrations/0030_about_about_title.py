# Generated by Django 2.2.8 on 2020-02-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_auto_20200213_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]