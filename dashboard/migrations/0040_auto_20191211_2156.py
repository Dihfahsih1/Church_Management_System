# Generated by Django 2.2.4 on 2019-12-11 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_members_visitors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledges',
            name='Pledge_Made_By',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Members'),
        ),
    ]