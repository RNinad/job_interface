# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=40)),
                ('DOB', models.CharField(max_length=12)),
                ('gender', models.CharField(max_length=7)),
                ('broad_qualification', models.CharField(max_length=10)),
                ('mobile_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=8)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naukri.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=40)),
                ('sector', models.CharField(max_length=20)),
                ('registration_no', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=40)),
                ('phone_no', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_sector', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('qualifications', models.CharField(max_length=40)),
                ('experience', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=15)),
                ('company_providing_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naukri.Company')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naukri.Job'),
        ),
    ]
