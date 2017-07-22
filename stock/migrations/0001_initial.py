# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-06 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbr', models.CharField(max_length=10)),
                ('predicted_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('yesterday_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('yesterday_date', models.DateField(auto_now_add=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('target_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('increased_bool', models.BooleanField(default=False)),
            ],
        ),
    ]