# Generated by Django 2.2.8 on 2020-02-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0059_expenditures_member_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditures',
            name='Notes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
