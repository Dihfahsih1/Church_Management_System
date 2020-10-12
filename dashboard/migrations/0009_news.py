# Generated by Django 2.2.8 on 2020-02-05 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_gallery_image_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('news', models.TextField()),
                ('Is_View_on_Web', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=20)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ('-date',),
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
    ]
