# Generated by Django 2.2.8 on 2021-05-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_user_get_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, default='2021-04-12', null=True),
        ),
    ]
