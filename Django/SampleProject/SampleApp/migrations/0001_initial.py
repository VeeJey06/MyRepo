# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-08 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmplyeeTable',
            fields=[
                ('emp_id', models.IntegerField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('emp_first_name', models.CharField(max_length=255)),
                ('emp_last_name', models.CharField(max_length=255)),
                ('emp_exp', models.IntegerField(max_length=2)),
            ],
        ),
    ]