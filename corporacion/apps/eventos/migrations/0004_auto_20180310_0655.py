# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-10 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20180309_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='evn_horaevn',
            field=models.TimeField(verbose_name='Hora del evento'),
        ),
    ]
