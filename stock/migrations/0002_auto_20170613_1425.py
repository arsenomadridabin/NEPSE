# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-13 14:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='company',
            name='increased_bool',
        ),
        migrations.RemoveField(
            model_name='company',
            name='predicted_price',
        ),
        migrations.RemoveField(
            model_name='company',
            name='target_price',
        ),
        migrations.RemoveField(
            model_name='company',
            name='yesterday_date',
        ),
        migrations.RemoveField(
            model_name='company',
            name='yesterday_price',
        ),
        migrations.AddField(
            model_name='company',
            name='low_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='max_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='min_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='no_of_transaction',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='sector_name',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='traded_share',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]