# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-07 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Box', '0002_remove_user_files_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_files',
            name='user_uploaded',
            field=models.CharField(default='MANGESH', max_length=50),
        ),
    ]