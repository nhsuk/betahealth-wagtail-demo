# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20160928_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simplepage',
            name='date',
        ),
    ]
