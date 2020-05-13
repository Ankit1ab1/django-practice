# Generated by Django 3.0.6 on 2020-05-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_mail', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=30)),
                ('job_desc', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
