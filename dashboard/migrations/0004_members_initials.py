# Generated by Django 2.2.8 on 2020-02-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200203_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Initials',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Pr.', 'Pr.'), ('Dr.', 'Dr.'), ('Eng.', 'Eng.')], max_length=100, null=True),
        ),
    ]
