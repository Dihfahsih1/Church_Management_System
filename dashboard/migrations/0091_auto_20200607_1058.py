# Generated by Django 2.2.8 on 2020-06-07 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0090_visitors_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidpledges',
            name='Pledge_Made_By_Visitor',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Visitors'),
        ),
        migrations.AddField(
            model_name='pledges',
            name='Pledge_Made_By_Visitor',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Visitors'),
        ),
        migrations.AddField(
            model_name='pledges',
            name='is_church_member',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=100, null=True),
        ),
    ]