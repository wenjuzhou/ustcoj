# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_auto_20170809_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='solved_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='trying_cnt',
            field=models.IntegerField(default=0),
        ),
    ]
