# Generated by Django 2.2.17 on 2021-03-02 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20210215_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='created_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='members',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
