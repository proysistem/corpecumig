# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-20 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ktg_detalle', models.CharField(max_length=15, verbose_name='Detalle')),
                ('ktg_abrevia', models.CharField(max_length=7, verbose_name='Abreviatura')),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciu_nombres', models.CharField(max_length=25, verbose_name='Nombre')),
                ('ciu_abrevia', models.CharField(max_length=10, verbose_name='Abreviatura')),
            ],
        ),
        migrations.CreateModel(
            name='Controlador',
            fields=[
                ('ctl_idcontr', models.AutoField(primary_key=True, serialize=False, verbose_name='Cód. del control de secuencia')),
                ('ctl_secue01', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 01 (Factura)')),
                ('ctl_secue02', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 02')),
                ('ctl_secue03', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 03')),
                ('ctl_secue04', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 04')),
                ('ctl_secue05', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 05 Nota/Crédito')),
                ('ctl_secue06', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 06 Nota/Débito')),
                ('ctl_secue07', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 07')),
                ('ctl_secue08', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 08')),
                ('ctl_secue09', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 09')),
                ('ctl_secue10', models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 10')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pai_detalle', models.CharField(max_length=25, verbose_name='Nombre')),
                ('pai_abrevia', models.CharField(max_length=10, verbose_name='Abreviatura')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_detalle', models.CharField(max_length=25, verbose_name='Nombre')),
                ('est_abrevia', models.CharField(max_length=10, verbose_name='Abreviatura')),
                ('est_capital', models.CharField(max_length=30, verbose_name='Capital')),
                ('est_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suc_codgsuc', models.PositiveIntegerField(db_index=True, unique=True, verbose_name='Cód.Sucursal')),
                ('suc_nombres', models.CharField(max_length=30, verbose_name='Nombre')),
                ('suc_abrevia', models.CharField(max_length=15, verbose_name='Abreviatura')),
                ('suc_direcci', models.CharField(max_length=45, verbose_name='Dirección')),
                ('suc_impuest', models.PositiveIntegerField(default=12, verbose_name='IVA/Impuesto %')),
                ('suc_statreg', models.CharField(max_length=1, verbose_name='Status del Registro')),
                ('suc_ciudads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Ciudad')),
                ('suc_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Pais')),
                ('suc_estados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Zipcodigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_idzipco', models.CharField(max_length=15, verbose_name='Código Postal')),
                ('zip_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Pais')),
                ('zip_estados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Provincia')),
                ('zip_idciuda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='sucursal',
            name='suc_zipcodg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Zipcodigo'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_sucrsal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parametros.Sucursal'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='ciu_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='ciu_estados',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Provincia'),
        ),
    ]