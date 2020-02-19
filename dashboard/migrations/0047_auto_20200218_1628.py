# Generated by Django 2.2.8 on 2020-02-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0046_buildingrenovation_archived_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingrenovation',
            name='Archived_Status',
            field=models.CharField(blank=True, choices=[('ARCHIVED', 'ARCHIVED'), ('UN-ARCHIVED', 'UN-ARCHIVED')], default='UN-ARCHIVED', max_length=100, null=True),
        ),
    ]