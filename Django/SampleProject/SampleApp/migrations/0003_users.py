# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-08 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SampleApp', '0002_auto_20210208_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
