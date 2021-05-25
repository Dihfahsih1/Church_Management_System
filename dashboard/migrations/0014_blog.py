# Generated by Django 2.2.8 on 2021-05-25 19:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_lwakiolimulamu_topic_or_sub_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=1200, null=True)),
                ('title', models.CharField(blank=True, max_length=1200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('details', ckeditor_uploader.fields.RichTextUploadingField()),
                ('reference_link', models.CharField(blank=True, max_length=120000, null=True)),
            ],
        ),
    ]
