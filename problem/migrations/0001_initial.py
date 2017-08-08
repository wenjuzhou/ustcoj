# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', markdownx.models.MarkdownxField()),
                ('input_description', markdownx.models.MarkdownxField()),
                ('output_description', markdownx.models.MarkdownxField()),
                ('hint', markdownx.models.MarkdownxField()),
                ('samples', jsonfield.fields.JSONField()),
                ('input_method', models.CharField(default='stdin', max_length=31)),
                ('output_method', models.CharField(default='stdout', max_length=31)),
                ('time_limit', models.IntegerField(default=1000, verbose_name='time limit (ms)')),
                ('memory_limit', models.IntegerField(default=256, verbose_name='memory limit (MB)')),
                ('testset_id', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='time to publish')),
                ('mod_time', models.DateTimeField(auto_now=True, verbose_name='time modified')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='time added')),
                ('public', models.BooleanField(default=False)),
                ('special_judge', models.BooleanField(default=False)),
                ('problem_id', models.IntegerField(db_index=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(to='problem.ProblemTag'),
        ),
    ]
