# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20160513_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255, verbose_name='作成者'),
        ),
    ]
