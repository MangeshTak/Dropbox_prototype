# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-08 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Box', '0004_auto_20171006_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='share_files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.CharField(max_length=300)),
                ('user_shared', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='user_files',
            name='Browse',
            field=models.FileField(upload_to='img/'),
        ),
    ]