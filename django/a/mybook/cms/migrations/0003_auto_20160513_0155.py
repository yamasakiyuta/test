# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-12 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20160512_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page',
            field=models.IntegerField(blank=True, max_length=255, verbose_name='作成者'),
        ),
    ]
