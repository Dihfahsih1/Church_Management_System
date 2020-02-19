# Generated by Django 2.2.8 on 2020-02-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_members_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Activity_Type',
            field=models.CharField(choices=[('Events', 'Events'), ('Church_Program', 'Church_Program')], default='Events', max_length=20),
        ),
        migrations.AddField(
            model_name='event',
            name='Day',
            field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='End_Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='Program_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='Start_Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_for',
            field=models.CharField(blank=True, choices=[('SuperAdmin', 'SuperAdmin'), ('Members', 'Members'), ('Secretary', 'Secretary'), ('Admin', 'Admin')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_place',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]