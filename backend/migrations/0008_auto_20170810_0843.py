# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 08:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20170807_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='release',
            field=models.DateField(default=datetime.date(2017, 8, 10), verbose_name='发布日期'),
        ),
    ]