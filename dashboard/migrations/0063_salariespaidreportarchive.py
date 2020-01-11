# Generated by Django 2.2.8 on 2020-01-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0062_paidpledges_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalariesPaidReportArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salary_Id', models.CharField(blank=True, max_length=200, null=True)),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Salary_Amount', models.IntegerField(default=0)),
                ('Month_being_cleared', models.DateField(blank=True, null=True)),
                ('Date_of_paying_salary', models.DateField(blank=True, null=True)),
                ('archivedmonth', models.CharField(max_length=100, null=True)),
                ('archivedyear', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]