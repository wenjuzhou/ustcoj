# Generated by Django 2.0.4 on 2018-05-25 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='group_create_permission',
        ),
    ]