# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=100)),
                ('collection', models.CharField(max_length=100)),
            ],
        ),
    ]
