# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-25 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asp_frsname', models.CharField(max_length=15, verbose_name='Primer Nombre')),
                ('asp_midname', models.CharField(max_length=15, verbose_name='Segundo Nombre')),
                ('asp_secmanp', models.CharField(max_length=25, verbose_name='Apellidos')),
                ('asp_secmanm', models.CharField(max_length=25, verbose_name='Apellidos')),
                ('asp_fechnac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('asp_direcci', models.CharField(max_length=50, verbose_name='Direccion Domiciliaria')),
                ('asp_zipcodg', models.CharField(blank=True, max_length=15, null=True, verbose_name='Cód. Postal')),
                ('asp_telefon', models.CharField(blank=True, max_length=15, verbose_name='Telefono')),
                ('asp_celular', models.CharField(blank=True, max_length=15, verbose_name='Celular')),
                ('asp_correoe', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('asp_imgclte', models.ImageField(blank=True, upload_to='clientes')),
                ('asp_rgunico', models.CharField(blank=True, max_length=20, verbose_name='Registro Unico')),
                ('asp_categor', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_frsname', models.CharField(max_length=15, verbose_name='Primer Nombre')),
                ('req_secname', models.CharField(max_length=25, verbose_name='Apellidos')),
                ('req_direcci', models.CharField(max_length=50, verbose_name='Dirección Domiciliaria')),
                ('req_zipcodg', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código postal')),
                ('req_correoe', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('req_fechmsj', models.DateTimeField(auto_now_add=True)),
                ('req_descrip', models.TextField(default='Solicito exposición', max_length=25, verbose_name='Titulo')),
                ('req_mensaje', models.CharField(max_length=220, verbose_name='Mensaje')),
                ('req_requier', models.BooleanField(default=True)),
            ],
        ),
    ]