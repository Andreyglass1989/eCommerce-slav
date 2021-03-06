# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-09 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dress',
            name='availability',
            field=models.BooleanField(default=False, verbose_name='\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='dress',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='dress',
            name='price',
            field=models.FloatField(verbose_name='\u0426\u0435\u043d\u0430, \u0433\u0440\u043d.'),
        ),
    ]
