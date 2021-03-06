# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-13 04:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cosocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cso_nombres', models.CharField(max_length=25, verbose_name='Primer Nombre')),
                ('cso_apellid', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('cso_fechnac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('cso_identif', models.CharField(db_index=True, max_length=15, unique=True, verbose_name='Id. del Co-socio')),
                ('cso_direcci', models.CharField(max_length=50, verbose_name='Direccion Domiciliaria')),
                ('cso_citynam', models.CharField(blank=True, max_length=30, null=True, verbose_name='Ciudad')),
                ('cso_statnam', models.CharField(blank=True, max_length=30, null=True, verbose_name='Estado / Porvincia')),
                ('cso_paisnam', models.CharField(blank=True, max_length=30, null=True, verbose_name='País')),
                ('cso_zipcodg', models.CharField(blank=True, max_length=15, null=True, verbose_name='Cód. Postal')),
                ('cso_telefon', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('cso_celular', models.CharField(blank=True, max_length=15, null=True, verbose_name='Celular')),
                ('cso_correoe', models.EmailField(blank=True, max_length=75, null=True, verbose_name='e-mail')),
                ('cso_imgfoto', models.ImageField(blank=True, null=True, upload_to='cosocio')),
                ('cso_imgidea', models.ImageField(blank=True, null=True, upload_to='cosocio')),
                ('cso_imgideb', models.ImageField(blank=True, null=True, upload_to='cosocio')),
                ('cso_rgunico', models.CharField(blank=True, max_length=20, verbose_name='Registro Unico')),
                ('cso_registr', models.CharField(blank=True, default='No', max_length=3, null=True)),
                ('cso_accions', models.PositiveIntegerField()),
                ('cso_fechreg', models.DateField(auto_now_add=True, verbose_name='Fecha de registración')),
                ('cso_categor', models.CharField(blank=True, default='0', max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_nombres', models.CharField(max_length=30, verbose_name='Nombre de la imagen')),
                ('img_detalle', models.CharField(max_length=75, verbose_name='Detalle de la imagen')),
                ('img_imagenx', models.ImageField(blank=True, upload_to='clientes')),
                ('img_fechreg', models.DateField(verbose_name='Fecha de registración')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soc_nombres', models.CharField(max_length=25, verbose_name='Primer Nombre')),
                ('soc_apellid', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('soc_fechnac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('soc_identif', models.CharField(db_index=True, max_length=15, unique=True, verbose_name='Id. del socio')),
                ('soc_direcci', models.CharField(max_length=50, verbose_name='Direccion Domiciliaria')),
                ('soc_citynam', models.CharField(blank=True, max_length=30, null=True, verbose_name='Ciudad')),
                ('soc_statnam', models.CharField(blank=True, max_length=30, null=True, verbose_name='Estado / Porvincia')),
                ('soc_paisnam', models.CharField(blank=True, max_length=30, null=True, verbose_name='País')),
                ('soc_zipcodg', models.CharField(blank=True, max_length=15, null=True, verbose_name='Cód. Postal')),
                ('soc_telefon', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('soc_celular', models.CharField(blank=True, max_length=15, null=True, verbose_name='Celular')),
                ('soc_correoe', models.EmailField(blank=True, max_length=75, null=True, verbose_name='e-mail')),
                ('soc_imgfoto', models.ImageField(blank=True, null=True, upload_to='socio')),
                ('soc_imgidea', models.ImageField(blank=True, null=True, upload_to='socio')),
                ('soc_imgideb', models.ImageField(blank=True, null=True, upload_to='socio')),
                ('soc_rgunico', models.CharField(blank=True, max_length=20, verbose_name='Registro Unico')),
                ('soc_registr', models.CharField(blank=True, default='No', max_length=3, null=True)),
                ('soc_accions', models.PositiveIntegerField()),
                ('soc_fechreg', models.DateField(auto_now_add=True, verbose_name='Fecha de registración')),
                ('soc_cosocio', models.BooleanField(default=False)),
                ('soc_categor', models.CharField(blank=True, default='0', max_length=3, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='imagen',
            name='img_corresp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='socios.Socio'),
        ),
        migrations.AddField(
            model_name='cosocio',
            name='cso_idsocio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='socios.Socio'),
        ),
    ]
