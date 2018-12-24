# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-24 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='analyse_of_market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.CharField(max_length=256)),
                ('origin', models.CharField(max_length=256)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'analyse_of_market',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.CharField(max_length=256)),
                ('view_number', models.CharField(max_length=16)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'Announcement',
            },
        ),
        migrations.CreateModel(
            name='industry_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.CharField(max_length=256)),
                ('origin', models.CharField(max_length=256)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'industry_information',
            },
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('user_icon', models.ImageField(upload_to='icons')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='web_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_name', models.TextField()),
                ('web_url', models.TextField()),
                ('web_type', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'web_list',
            },
        ),
    ]
