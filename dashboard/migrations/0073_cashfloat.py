# Generated by Django 2.2.8 on 2020-03-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0072_auto_20200303_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashFloat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, null=True)),
                ('Amount', models.IntegerField(default=0)),
                ('Notes', models.TextField(blank=True, max_length=100000, null=True)),
            ],
        ),
    ]
