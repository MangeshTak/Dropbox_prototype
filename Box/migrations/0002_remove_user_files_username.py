# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-07 00:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Box', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_files',
            name='Username',
        ),
    ]
