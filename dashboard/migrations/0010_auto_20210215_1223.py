# Generated by Django 2.2.17 on 2021-02-15 12:23

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_cashfloat_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
