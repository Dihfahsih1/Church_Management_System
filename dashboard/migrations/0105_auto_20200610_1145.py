# Generated by Django 2.2.8 on 2020-06-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0104_members_full_named'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='Email',
            field=models.EmailField(default='email@email.com', max_length=254),
            preserve_default=False,
        ),
    ]
