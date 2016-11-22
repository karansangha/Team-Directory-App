# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20161122_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='person',
            name='github',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='person',
            name='responsibilities',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='twitter',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
