from django.db import models
from apps.parametros.models import Pais, Provincia, Ciudad, Zipcodigo, Sucursal, Categoria
from apps.users.models import User
from apps.parametros.choices import TIPO_MOV_CHOICES
# Create your models here.


class Moneda(models.Model):

    mda_detalle = models.CharField('Detalle', max_length=25)
    mda_abrevia = models.CharField('Abreviatura', max_length=7)
    mda_cotizac = models.DecimalField('Cotización ', max_digits=11, decimal_places=4)
    mda_mndofic = models.CharField('Moneda Oficial', max_length=25)
    mda_abrofic = models.CharField('Abrev. Moneda oficial', max_length=15)

    def __str__(self):
        return "%s" % (self.mda_detalle)


class Tipodocum(models.Model):
    tpd_coddocm = models.CharField('Cód. de documento', max_length=18, unique=True, db_index=True)
    tpd_referen = models.CharField('Referencia', max_length=10)
    tpd_nombres = models.CharField("Nombre", max_length=25)
    tpd_abrevia = models.CharField("Abreviatura", max_length=10)

    def __str__(self):
        return "%s %s" % (self.tpd_coddocm, self.tpd_nombres)


class Tabelemento(models.Model):
    tug_codelem = models.CharField('Cód. de documento', max_length=10, unique=True, db_index=True)
    tug_referen = models.CharField('Referencia', max_length=15, null=True, blank=True)
    tug_detalle = models.CharField("Detalle", max_length=35)
    tug_tranori = models.CharField("Origen de Transacción", max_length=10)
    tug_tranref = models.CharField("Origen: Cód.referencia", max_length=15)
    tug_trannun = models.IntegerField("Origen: Núm.referencia")
    tug_trandet = models.CharField("Origen detalle", max_length=15)
    tug_tranprm = models.CharField("Origen: parametros", max_length=15)
    tug_observa = models.CharField('Observaciones', max_length=15, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.tpd_coddocm, self.tpd_nombres)


class Cajera(models.Model):

    cjr_frsname = models.CharField('Primer Nombre', max_length=15)
    cjr_midname = models.CharField('Segundo Nombre', max_length=15)
    cjr_lasname = models.CharField('Apellidos', max_length=25)
    cjr_fechnac = models.DateField('Fecha de Nacimiento')
    cjr_direcci = models.CharField('Direccion Domiciliaria', max_length=50)
    cjr_ciudade = models.ForeignKey(Ciudad, null=True, blank=True)
    cjr_estados = models.ForeignKey(Provincia, null=True, blank=True)
    cjr_country = models.ForeignKey(Pais, null=True, blank=True)
    cjr_zipcodg = models.ForeignKey(Zipcodigo, null=True, blank=True)
    cjr_telefon = models.CharField('Telefono', max_length=15)
    cjr_celular = models.CharField('Celular', max_length=15)
    cjr_correoe = models.EmailField('e-mail')
    cjr_imgcjer = models.ImageField(upload_to="cajeras")
    cjr_rgunico = models.IntegerField('Registro Unico')
    cjr_categor = models.ForeignKey(Categoria, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.cjr_frsname, self.cjr_lasname)


class Caja(models.Model):

    cja_numcaja = models.IntegerField('Núm. de Caja', primary_key=True)
    cja_plancta = models.OneToOneField('Plancuenta', unique=True, db_index=True)
    cja_monedas = models.ForeignKey(Moneda, null=True, blank=True)
    cja_cotizac = models.DecimalField('Cotización', max_digits=15, decimal_places=4)
    cja_fchultm = models.DateField('Fecha de último movimiento')
    cja_cajeras = models.ForeignKey(Cajera, null=True, blank=True)
    cja_inicash = models.DecimalField('Saldo Inic.Cash', max_digits=15, decimal_places=4)
    cja_ingcash = models.DecimalField('Ingresos Cash', max_digits=15, decimal_places=4)
    cja_egrcash = models.DecimalField('Egresos Cash', max_digits=15, decimal_places=4)
    cja_salcash = models.DecimalField('Saldo Actual Cash', max_digits=15, decimal_places=4)
    cja_inicchq = models.DecimalField('Saldo Inic.Cheq.', max_digits=15, decimal_places=4)
    cja_ingrchq = models.DecimalField('Ingresos Cheq.', max_digits=15, decimal_places=4)
    cja_egrechq = models.DecimalField('Egresos Cheq.', max_digits=15, decimal_places=4)
    cja_saldchq = models.DecimalField('Saldo Actual Cheq.', max_digits=15, decimal_places=4)
    cja_inictjc = models.DecimalField('Saldo Inic.T/CR.', max_digits=15, decimal_places=4)
    cja_ingrtjc = models.DecimalField('Ingresos T/CR.', max_digits=15, decimal_places=4)
    cja_egretjc = models.DecimalField('Egresos T/CR.', max_digits=15, decimal_places=4)
    cja_saldtjc = models.DecimalField('Saldo Actual T/CR.', max_digits=15, decimal_places=4)
    cja_inicred = models.DecimalField('Saldo Inic.Cred.', max_digits=15, decimal_places=4)
    cja_ingcred = models.DecimalField('Ingresos Cred.', max_digits=15, decimal_places=4)
    cja_egrcred = models.DecimalField('Egresos Cred.', max_digits=15, decimal_places=4)
    cja_salcred = models.DecimalField('Saldo Actual Cred.', max_digits=15, decimal_places=4)
    cja_inicotr = models.DecimalField('Saldo Inic.Otro', max_digits=15, decimal_places=4)
    cja_ingrotr = models.DecimalField('Ingresos Otro', max_digits=15, decimal_places=4)
    cja_egreotr = models.DecimalField('Egresos Otro', max_digits=15, decimal_places=4)
    cja_saldotr = models.DecimalField('Saldo Actual Otro', max_digits=15, decimal_places=4)
    cja_fcharqe = models.DateField('Fecha de Arqueo/Caja')
    cja_numarqe = models.IntegerField('Núm. De Arqueo')
    cja_arqefec = models.DecimalField('Arq. Cash', max_digits=15, decimal_places=4)
    cja_arqcheq = models.DecimalField('Arq. Cheq.', max_digits=15, decimal_places=4)
    cja_arqtjcr = models.DecimalField('Arq. T/CR.', max_digits=15, decimal_places=4)
    cja_arqcred = models.DecimalField('Arq. Crédito', max_digits=15, decimal_places=4)
    cja_arqotro = models.DecimalField('Arq.Otros', max_digits=15, decimal_places=4)

    def __str__(self):
        return "%s" % (self.cja_numcaja)


class Movicaja(models.Model):
    mcj_compcja = models.IntegerField('Núm. comprobante de caja', unique=True, db_index=True)
    mcj_sucursa = models.ForeignKey(Sucursal)
    mcj_monedas = models.ForeignKey(Moneda)
    mcj_cotizac = models.DecimalField('Cotización', max_digits=11, decimal_places=4)
    mcj_fechmov = models.DateField('Fecha')
    mcj_cajanum = models.ForeignKey(Caja)
    mcj_cajeras = models.ForeignKey(Cajera)
    mcj_tipomov = models.PositiveIntegerField("Tipo de movimiento", choices=TIPO_MOV_CHOICES)
    mcj_tpodocu = models.ForeignKey(Tipodocum)
    mcj_numdocu = models.IntegerField('Documento origen')
    mcj_plancta = models.OneToOneField('Plancuenta', editable=False)
    mcj_comprob = models.OneToOneField('Comprobante', editable=False)
    mcj_valcash = models.DecimalField('Cash', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_valcheq = models.DecimalField('Cheque', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_valtjcr = models.DecimalField('T./Crédito', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_valcred = models.DecimalField('Crédito personal', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_valotro = models.DecimalField('Internet (Paypal)', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_imgcomp = models.ImageField(upload_to="comprobcaja", blank=True)

    def __str__(self):
        return "%s" % (self.mcj_compcja)


class Plancuenta(models.Model):

    class Meta:
        verbose_name = "Plancuenta"
        verbose_name_plural = "Plancuentas"
    plc_ncuenta = models.CharField('Núm. Planctas', max_length=18, primary_key=True)
    plc_cuenta1 = models.CharField('Cta. de nivel 1', max_length=1)
    plc_cuenta2 = models.CharField('Cta. de nivel 2', max_length=1)
    plc_cuenta3 = models.CharField('Cta. de nivel 3', max_length=1)
    plc_cuenta4 = models.CharField('Cta. de nivel 4', max_length=2)
    plc_auxili1 = models.CharField('Auxiliar de nivel-1', max_length=2)
    plc_auxili2 = models.CharField('Auxiliar de nivel-2', max_length=2)
    plc_auxili3 = models.CharField('Auxiliar de nivel-3', max_length=2)
    plc_detalle = models.CharField('Nombre de la cta.', max_length=40)
    plc_ctabaln = models.CharField('Cuenta  de baalance', max_length=1)
    plc_ctanexo = models.CharField('Cta. para los anexos', max_length=1)
    plc_ctarsul = models.CharField('Cta. para resultados (p/g)', max_length=1)
    plc_ctamyor = models.CharField('Cta. para mayotizarce', max_length=1)
    plc_nivlcta = models.CharField('Nivel Cta. 1-7', max_length=1, default='0')
    plc_tipocta = models.CharField('Naturaleza de cta D/C', max_length=1)

    def __str__(self):
        return "%s %s" % (self.plc_ncuenta, self.plc_detalle)


class Centrocosto(models.Model):

    class Meta:
        verbose_name = "Centrocosto"
        verbose_name_plural = "Centrocostos"

    cos_ncuenta = models.CharField('Núm. Centro de costo', max_length=18, unique=True, db_index=True)
    cos_cuenta1 = models.CharField('Cta. de nivel 1', max_length=1)
    cos_cuenta2 = models.CharField('Cta. de nivel 2', max_length=1)
    cos_cuenta3 = models.CharField('Cta. de nivel 3', max_length=1)
    cos_cuenta4 = models.CharField('Cta. de nivel 4', max_length=2)
    cos_auxili1 = models.CharField('Auxiliar de nivel-1', max_length=2)
    cos_auxili2 = models.CharField('Auxiliar de nivel-2', max_length=2)
    cos_auxili3 = models.CharField('Auxiliar de nivel-3', max_length=2)
    cos_detalle = models.CharField('Nombre de la cta.', max_length=40)
    cos_ctabaln = models.CharField('Cuenta  de baalance', max_length=25)
    cos_ctanexo = models.CharField('Cta. para los anexos', max_length=25)
    cos_ctarsul = models.CharField('Cta. para resultados (p/g)', max_length=1)
    cos_ctamyor = models.CharField('Cta. para mayotizarce', max_length=1)
    cos_nivlcta = models.CharField('Nivel Cta. 1 a 7', max_length=1)
    cos_tipocta = models.CharField('Naturaleza de cta D/C', max_length=1)

    def __str__(self):
        return "%s %s" % (self.cos_ncuenta, self.cos_detalle)


class Saldocontab(models.Model):

    class Meta:
        verbose_name = "Saldocontab"
        verbose_name_plural = "Saldocontabs"

    slc_ncuenta = models.OneToOneField(Plancuenta, unique=True, db_index=True)
    slc_sucursa = models.OneToOneField(Sucursal)

    slc_saldinc = models.DecimalField('Saldo inicial', max_digits=13, decimal_places=4, blank=True, null=True)
    slc_ingreso = models.DecimalField('Ingresos', max_digits=13, decimal_places=4, blank=True, null=True)
    slc_egresos = models.DecimalField('Egresos', max_digits=13, decimal_places=4, blank=True, null=True)
    slc_saldact = models.DecimalField('Saldo Actual', max_digits=13, decimal_places=4, blank=True, null=True)

    slc_inici01 = models.DecimalField('Saldo inici-01', max_digits=13, decimal_places=4, null=True)
    slc_inici02 = models.DecimalField('Saldo inici-02', max_digits=13, decimal_places=4, null=True)
    slc_inici03 = models.DecimalField('Saldo inici-03', max_digits=13, decimal_places=4, null=True)
    slc_inici04 = models.DecimalField('Saldo inici-04', max_digits=13, decimal_places=4, null=True)
    slc_inici05 = models.DecimalField('Saldo inici-05', max_digits=13, decimal_places=4, null=True)
    slc_inici06 = models.DecimalField('Saldo inici-06', max_digits=13, decimal_places=4, null=True)
    slc_inici07 = models.DecimalField('Saldo inici-07', max_digits=13, decimal_places=4, null=True)
    slc_inici08 = models.DecimalField('Saldo inici-08', max_digits=13, decimal_places=4, null=True)
    slc_inici09 = models.DecimalField('Saldo inici-09', max_digits=13, decimal_places=4, null=True)
    slc_inici10 = models.DecimalField('Saldo inici-10', max_digits=13, decimal_places=4, null=True)
    slc_inici11 = models.DecimalField('Saldo inici-11', max_digits=13, decimal_places=4, null=True)
    slc_inici12 = models.DecimalField('Saldo inici-12', max_digits=13, decimal_places=4, null=True)

    slc_ingre01 = models.DecimalField('Saldo ingre-01', max_digits=13, decimal_places=4, null=True)
    slc_ingre02 = models.DecimalField('Saldo ingre-02', max_digits=13, decimal_places=4, null=True)
    slc_ingre03 = models.DecimalField('Saldo ingre-03', max_digits=13, decimal_places=4, null=True)
    slc_ingre04 = models.DecimalField('Saldo ingre-04', max_digits=13, decimal_places=4, null=True)
    slc_ingre05 = models.DecimalField('Saldo ingre-05', max_digits=13, decimal_places=4, null=True)
    slc_ingre06 = models.DecimalField('Saldo ingre-06', max_digits=13, decimal_places=4, null=True)
    slc_ingre07 = models.DecimalField('Saldo ingre-07', max_digits=13, decimal_places=4, null=True)
    slc_ingre08 = models.DecimalField('Saldo ingre-08', max_digits=13, decimal_places=4, null=True)
    slc_ingre09 = models.DecimalField('Saldo ingre-09', max_digits=13, decimal_places=4, null=True)
    slc_ingre10 = models.DecimalField('Saldo ingre-10', max_digits=13, decimal_places=4, null=True)
    slc_ingre11 = models.DecimalField('Saldo ingre-11', max_digits=13, decimal_places=4, null=True)
    slc_ingre12 = models.DecimalField('Saldo ingre-12', max_digits=13, decimal_places=4, null=True)

    slc_egres01 = models.DecimalField('Saldo egres-01', max_digits=13, decimal_places=4, null=True)
    slc_egres02 = models.DecimalField('Saldo egres-02', max_digits=13, decimal_places=4, null=True)
    slc_egres03 = models.DecimalField('Saldo egres-03', max_digits=13, decimal_places=4, null=True)
    slc_egres04 = models.DecimalField('Saldo egres-04', max_digits=13, decimal_places=4, null=True)
    slc_egres05 = models.DecimalField('Saldo egres-05', max_digits=13, decimal_places=4, null=True)
    slc_egres06 = models.DecimalField('Saldo egres-06', max_digits=13, decimal_places=4, null=True)
    slc_egres07 = models.DecimalField('Saldo egres-07', max_digits=13, decimal_places=4, null=True)
    slc_egres08 = models.DecimalField('Saldo egres-08', max_digits=13, decimal_places=4, null=True)
    slc_egres09 = models.DecimalField('Saldo egres-09', max_digits=13, decimal_places=4, null=True)
    slc_egres10 = models.DecimalField('Saldo egres-10', max_digits=13, decimal_places=4, null=True)
    slc_egres11 = models.DecimalField('Saldo egres-11', max_digits=13, decimal_places=4, null=True)
    slc_egres12 = models.DecimalField('Saldo egres-12', max_digits=13, decimal_places=4, null=True)

    slc_actua01 = models.DecimalField('Saldo actua-01', max_digits=13, decimal_places=4, null=True)
    slc_actua02 = models.DecimalField('Saldo actua-02', max_digits=13, decimal_places=4, null=True)
    slc_actua03 = models.DecimalField('Saldo actua-03', max_digits=13, decimal_places=4, null=True)
    slc_actua04 = models.DecimalField('Saldo actua-04', max_digits=13, decimal_places=4, null=True)
    slc_actua05 = models.DecimalField('Saldo actua-05', max_digits=13, decimal_places=4, null=True)
    slc_actua06 = models.DecimalField('Saldo actua-06', max_digits=13, decimal_places=4, null=True)
    slc_actua07 = models.DecimalField('Saldo actua-07', max_digits=13, decimal_places=4, null=True)
    slc_actua08 = models.DecimalField('Saldo actua-08', max_digits=13, decimal_places=4, null=True)
    slc_actua09 = models.DecimalField('Saldo actua-09', max_digits=13, decimal_places=4, null=True)
    slc_actua10 = models.DecimalField('Saldo actua-10', max_digits=13, decimal_places=4, null=True)
    slc_actua11 = models.DecimalField('Saldo actua-11', max_digits=13, decimal_places=4, null=True)
    slc_actua12 = models.DecimalField('Saldo actua-12', max_digits=13, decimal_places=4, null=True)

    def __str__(self):
        return "%s %s" % (self.slc_ncuenta, self.slc_sucursa)


class Comprobante(models.Model):

    class Meta:
        verbose_name = "Comprobante"
        verbose_name_plural = "Comprobantes"

    cmp_comprob = models.CharField('Núm. Comprobante', max_length=18, unique=True, db_index=True)
    cmp_ncuenta = models.ForeignKey(Plancuenta, verbose_name="Cuenta/Plan de Ctas.")
    cmp_fechcmp = models.DateField('Fecha de comprobante')
    cmp_usernam = models.ForeignKey(User)
    cmp_sucursa = models.ForeignKey(Sucursal)
    cmp_origpro = models.CharField('Origen del proceso=programa de origen', max_length=35)
    cmp_origtra = models.CharField('Origen de transacción (F=Factura,C=Compra,Cheques, hacer Tabla)', max_length=1)
    cmp_numorig = models.CharField('Numero o ref. de origen', max_length=25)
    cmp_tpoenti = models.CharField('Tipo de entidad (C=Cliente,P=Proveedor,hacer Tabla)', max_length=1)
    cmp_entidad = models.CharField('Código de entidad', max_length=15)
    cmp_mondalt = models.ForeignKey(Moneda, verbose_name='Moneda alterna', null=True, blank=True)
    cmp_mondaof = models.CharField('Moneda Oficial', max_length=10, null=True, blank=True, default='USD.')
    cmp_cotizac = models.DecimalField('Cotización', max_digits=9, decimal_places=2, null=True, blank=True)
    cmp_cajanum = models.ForeignKey(Caja, verbose_name='Núm. de caja', null=True, blank=True)
    cmp_cajeras = models.ForeignKey(Cajera, verbose_name='Cód. de Cajera', null=True, blank=True)
    cmp_detalle = models.CharField('Detalle del movimiento', max_length=40)
    cmp_cantida = models.DecimalField('Cantidad', max_digits=13, decimal_places=2, null=True, blank=True)
    cmp_tpomovi = models.CharField('Tipo de Movimiento D=Débito, C=Credito, I=Inicial', max_length=1)
    cmp_valores = models.DecimalField('Valor', max_digits=15, decimal_places=2, null=True, blank=True)
    cmp_nivlcta = models.IntegerField('Nivel de cta.')
    cmp_periodo = models.IntegerField('Periodo contable')
    cmp_costord = models.IntegerField('Núm. de Orden costo')
    cmp_costcta = models.ForeignKey(Centrocosto, verbose_name='Cuenta/Centro de costos')
    cmp_imgcomp = models.ImageField(upload_to="comprobante", blank=True)
    cmp_statreg = models.CharField('Estado del Reg.', max_length=1)
    # Estado/Regist(0-1-2-3-4-5)
    # Reg.Inactivo.<╜ | | | | |
    # Reg.Activo...<--+ | | | |
    # Reg.Mayorizad<----+ | | |
    # Rep.Inconsist<------+ | |
    # Reg.Eliminado<--------+ |
    # Reg.Desconocd<----------+

    def __str__(self):
        pass
