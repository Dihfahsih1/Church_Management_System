# Generated by Django 2.2.8 on 2020-02-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20200206_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'default_permissions': ('view', 'add', 'change', 'delete'), 'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'default_permissions': ('view', 'add', 'change', 'delete'), 'ordering': ['-date'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='pledgescashedout',
            name='Item_That_Needs_Pledges',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
