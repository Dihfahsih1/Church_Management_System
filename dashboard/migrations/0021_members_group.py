# Generated by Django 2.2.8 on 2020-02-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20200207_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Group',
            field=models.CharField(blank=True, choices=[('God is Able', 'God is Able'), ('Winners', 'Winners'), ('Overcomers', 'Overcomers'), ('Biyinzika', 'Biyinzika'), ('Victors', 'Victors'), ('Issachar', 'Issachar')], default='God Is Able', max_length=100, null=True),
        ),
    ]
