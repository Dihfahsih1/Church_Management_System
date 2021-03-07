# Generated by Django 2.2.8 on 2021-03-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_themeoftheyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, max_length=20000, null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='members',
            name='Photo',
            field=models.ImageField(blank=True, max_length=20000, null=True, upload_to='avatars/'),
        ),
    ]