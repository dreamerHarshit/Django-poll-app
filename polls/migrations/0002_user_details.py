# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateTimeField(verbose_name=b'date_of_birth')),
                ('age', models.IntegerField(verbose_name=b'Enter_Age')),
                ('maritalstatus', models.BooleanField(default=False)),
            ],
        ),
    ]