# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0014_auto_20180414_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermovies',
            name='c_time',
            field=models.IntegerField(default=0),
        ),
    ]