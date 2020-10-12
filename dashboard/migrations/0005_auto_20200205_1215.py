# Generated by Django 2.2.8 on 2020-02-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_members_initials'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Is_View_on_Web',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='staffdetails',
            name='Is_View_on_Web',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=20, null=True),
        ),
    ]
