# Generated by Django 2.2.8 on 2020-07-04 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0109_auto_20200704_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledges',
            name='Pledge_Made_By',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Members'),
        ),
        migrations.AlterField(
            model_name='pledges',
            name='Pledge_Made_By_Visitor',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Visitors'),
        ),
        migrations.AlterField(
            model_name='pledges',
            name='Reason',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.PledgeItem'),
        ),
        migrations.AlterField(
            model_name='pledges',
            name='is_church_member',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='First_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='Second_Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
