# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-31 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20170731_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.SmallIntegerField(default=1),
        ),
    ]