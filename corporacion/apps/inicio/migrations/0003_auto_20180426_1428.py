# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-26 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_aspirante_solicitud'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aspirante',
            old_name='asp_secmanm',
            new_name='asp_apellid',
        ),
        migrations.RemoveField(
            model_name='aspirante',
            name='asp_frsname',
        ),
        migrations.RemoveField(
            model_name='aspirante',
            name='asp_midname',
        ),
        migrations.RemoveField(
            model_name='aspirante',
            name='asp_secmanp',
        ),
        migrations.AddField(
            model_name='aspirante',
            name='asp_nombres',
            field=models.CharField(default=1, max_length=25, verbose_name='Primer Nombre'),
            preserve_default=False,
        ),
    ]
