# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
