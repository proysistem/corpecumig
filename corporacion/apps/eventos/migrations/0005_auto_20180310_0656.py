# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-10 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20180310_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='evn_horaevn',
            field=models.TimeField(verbose_name='Hora del evento'),
        ),
    ]
