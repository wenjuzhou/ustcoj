# Generated by Django 2.0.4 on 2018-05-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_group_create_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='connect_way',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
