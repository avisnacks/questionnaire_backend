# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-27 04:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('choice', '0002_auto_20170808_0909'),
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='value')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='choice.Choice')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.City')),
            ],
        ),
    ]
