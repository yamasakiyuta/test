# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20160516_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Github',
            field=models.CharField(blank=True, max_length=255, verbose_name='Github'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255, verbose_name='著者名'),
        ),
    ]
