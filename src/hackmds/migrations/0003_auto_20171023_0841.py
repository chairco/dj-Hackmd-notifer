# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackmds', '0002_auto_20171022_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='content',
            field=models.TextField(max_length=10000, null=True, verbose_name='content'),
        ),
    ]
