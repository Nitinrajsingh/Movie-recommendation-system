# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0021_auto_20180416_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermovies',
            name='c_rating',
            field=models.FloatField(default=-1),
        ),
    ]