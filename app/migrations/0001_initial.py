# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id_friend', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'friend',
            },
        ),
    ]