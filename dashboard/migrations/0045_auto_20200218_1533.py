# Generated by Django 2.2.8 on 2020-02-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0044_buildingrenovation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingrenovation',
            name='Other_Notes',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]