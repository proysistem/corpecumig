# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-10 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20180309_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='evn_fechaev',
            field=models.DateField(verbose_name='Fecha deEvento'),
        ),
    ]
