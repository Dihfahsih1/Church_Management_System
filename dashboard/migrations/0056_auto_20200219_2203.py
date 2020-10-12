# Generated by Django 2.2.8 on 2020-02-19 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0055_expenditures_reason_filtering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, null=True)),
                ('Service', models.CharField(blank=True, choices=[('Home Cell Service', 'Home Cell Service'), ('Youth Service', 'Youth Service'), ('Wednesday Service', 'Wednesday Service'), ('Bible Study Service', 'Bible Study Service'), ('Friday Overnight', 'Friday Overnight'), ('Sunday First Service', 'Sunday First Service'), ('Sunday Second Service', 'Sunday Second Service'), ('Sunday Third Service', 'Sunday Third Service')], max_length=100, null=True)),
                ('Amount', models.IntegerField()),
                ('Archived_Status', models.CharField(blank=True, choices=[('ARCHIVED', 'ARCHIVED'), ('NOT-ARCHIVED', 'NOT-ARCHIVED')], default='NOT-ARCHIVED', max_length=100, null=True)),
                ('Revenue_filter', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Donations',
        ),
        migrations.DeleteModel(
            name='DonationsReportArchive',
        ),
        migrations.DeleteModel(
            name='ExpensesReportArchive',
        ),
        migrations.DeleteModel(
            name='GeneralExpensesReportArchive',
        ),
        migrations.DeleteModel(
            name='Offerings',
        ),
        migrations.DeleteModel(
            name='OfferingsReportArchive',
        ),
        migrations.RemoveField(
            model_name='seeds',
            name='Seed_Made_By',
        ),
        migrations.RemoveField(
            model_name='seedsreportarchive',
            name='Seed_Made_By',
        ),
        migrations.DeleteModel(
            name='SundryReportArchive',
        ),
        migrations.RemoveField(
            model_name='thanksgiving',
            name='Thanks_Giving_By',
        ),
        migrations.RemoveField(
            model_name='thanksgivingreportarchive',
            name='Thanks_Giving_By',
        ),
        migrations.RemoveField(
            model_name='tithes',
            name='Tithe_Made_By',
        ),
        migrations.RemoveField(
            model_name='tithesreportarchive',
            name='Tithe_Made_By',
        ),
        migrations.RemoveField(
            model_name='allowance',
            name='Month',
        ),
        migrations.RemoveField(
            model_name='allowancereportarchive',
            name='Month',
        ),
        migrations.AlterField(
            model_name='buildingrenovation',
            name='Service',
            field=models.CharField(choices=[('Home Cell Service', 'Home Cell Service'), ('Youth Service', 'Youth Service'), ('Wednesday Service', 'Wednesday Service'), ('Bible Study Service', 'Bible Study Service'), ('Friday Overnight', 'Friday Overnight'), ('Sunday First Service', 'Sunday First Service'), ('Sunday Second Service', 'Sunday Second Service'), ('Sunday Third Service', 'Sunday Third Service')], max_length=100),
        ),
        migrations.AlterField(
            model_name='members',
            name='Education_Level',
            field=models.CharField(blank=True, choices=[('Masters', 'Master'), ('Degree', 'Degree'), ('Diploma', 'Diploma'), ('Certificate', 'Certificate')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Seeds',
        ),
        migrations.DeleteModel(
            name='SeedsReportArchive',
        ),
        migrations.DeleteModel(
            name='ThanksGiving',
        ),
        migrations.DeleteModel(
            name='ThanksGivingReportArchive',
        ),
        migrations.DeleteModel(
            name='Tithes',
        ),
        migrations.DeleteModel(
            name='TithesReportArchive',
        ),
        migrations.AddField(
            model_name='revenues',
            name='Member_Name',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Members'),
        ),
    ]
