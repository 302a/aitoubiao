# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-27 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20181225_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_icon',
            field=models.ImageField(null=True, upload_to='icons'),
        ),
    ]