# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-11 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0008_auto_20181011_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldvalue',
            name='raw_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]