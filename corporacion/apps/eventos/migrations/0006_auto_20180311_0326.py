# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-11 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20180310_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='evn_fechaev',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='eml_fechmsj',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
