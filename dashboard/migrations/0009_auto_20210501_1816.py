# Generated by Django 2.2.8 on 2021-05-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_lwakiolimulamu_topic_or_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='Ministry_Involved_In',
            field=models.CharField(blank=True, choices=[('Pastoral', 'Pastoral'), ('Discipleship', 'Discipleship'), ('Worship Team', 'Worship Team'), ('Ushering', 'Ushering'), ('Orchestra', 'Orchestra'), ('Youth Ministry', 'Youth Ministry'), ('Wells Of Hope', 'Wells Of Hope'), ('Envangelism Ministry', 'Envangelism Ministry'), ('Intercession Ministry', 'Intercession Ministry'), ('Teens', 'Teens')], default='Discipleship', max_length=100, null=True),
        ),
    ]
