# Generated by Django 2.2.8 on 2021-05-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20210427_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='lwakiolimulamu',
            name='topic_or_sub_title',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
