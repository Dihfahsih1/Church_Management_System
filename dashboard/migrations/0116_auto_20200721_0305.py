# Generated by Django 2.2.8 on 2020-07-21 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0115_pledges_nameofpledgee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledges',
            old_name='Pledge_Id',
            new_name='PledgeItem',
        ),
    ]
