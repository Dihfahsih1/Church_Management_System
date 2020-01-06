# Generated by Django 2.2.8 on 2020-01-06 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0047_auto_20200106_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tithes',
            name='AmountInWords',
        ),
        migrations.RemoveField(
            model_name='tithes',
            name='DayOfTheWeek',
        ),
        migrations.RemoveField(
            model_name='tithes',
            name='TitheMadeBy',
        ),
        migrations.RemoveField(
            model_name='tithesreportarchive',
            name='Day',
        ),
        migrations.RemoveField(
            model_name='tithesreportarchive',
            name='Name',
        ),
        migrations.AddField(
            model_name='tithes',
            name='Tithe_Made_By',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Members'),
        ),
        migrations.AddField(
            model_name='tithesreportarchive',
            name='Tithe_Made_By',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Members'),
        ),
        migrations.AlterField(
            model_name='offerings',
            name='Service',
            field=models.CharField(choices=[('Home Cell Service', 'Home Cell Service'), ('Youth Service', 'Youth Service'), ('Wednesday Service', 'Wednesday Service'), ('Bible Study Service', 'Bible Study Service'), ('Friday Overnight', 'Friday Overnight'), ('SundayFirst Service', 'Sunday First Service'), ('Sunday Second Service', 'Sunday Second Service'), ('Sunday Third Service', 'Sunday Third Service')], max_length=100),
        ),
    ]
