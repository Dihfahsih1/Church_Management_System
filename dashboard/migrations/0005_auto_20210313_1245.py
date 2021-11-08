# Generated by Django 2.2.8 on 2021-03-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210308_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='Education_Level',
            field=models.CharField(blank=True, choices=[('Masters', 'Master'), ('Degree', 'Degree'), ('Diploma', 'Diploma'), ('A_Level_Graduate', 'A_Level_Graduate'), ('O_Level_Graduate', 'O_Level_Graduate'), ('Primary_Graduate', 'Primary_Graduate'), ('Still_Studying', 'Still_Studying'), ('None', 'None')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='Home_Cell',
            field=models.CharField(blank=True, choices=[('Church Zone', 'Church Zone'), ('Kabira Zone', 'Kabira Zone'), ('Katuba Zone', 'Katuba Zone'), ('Kafunda Zone', 'Kafunda Zone'), ('Lugoba Zone', 'Lugoba Zone'), ('Katooke Zone', 'Katooke Zone'), ('Kazo Zone', 'Kazo Zone'), ('Gombolola Zone', 'Gombolola Zone'), ('Kawaala Zone', 'Kawaala Zone'), ('Bombo Rd Zone', 'Bombo Rd Zone'), ('Kampala Metropolitan', 'Kampala Metropolitan')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='Ministry_Involved_In',
            field=models.CharField(blank=True, choices=[('Pastoral', 'Pastoral'), ('Discipleship', 'Discipleship'), ('Worship Team', 'Worship Team'), ('Ushering', 'Ushering'), ('Orchestra', 'Orchestra'), ('Youth Ministry', 'Youth Ministry'), ('Envangelism Ministry', 'Envangelism Ministry'), ('Intercession Ministry', 'Intercession Ministry'), ('Teens', 'Teens')], default='Discipleship', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='Education_Level',
            field=models.CharField(blank=True, choices=[('Masters', 'Master'), ('Degree', 'Degree'), ('Diploma', 'Diploma'), ('A_Level_Graduate', 'A_Level_Graduate'), ('O_Level_Graduate', 'O_Level_Graduate'), ('Primary_Graduate', 'Primary_Graduate'), ('Still_Studying', 'Still_Studying'), ('None', 'None')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default.png', max_length=20000, null=True, upload_to='avatars/'),
        ),
    ]
