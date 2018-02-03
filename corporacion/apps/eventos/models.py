from django.db import models


class Zipcodigo(models.Model):
    zip_idzipco = models.CharField("Código Postal", max_length=15, primary_key=True)
    zip_country = models.TextField('Pais', max_length=5)
    zip_estddet = models.TextField('Estado', max_length=30)
    zip_estdabr = models.TextField('Estado', max_length=5)
    zip_condado = models.TextField('Condado', max_length=35)
    zip_ciuddet = models.TextField('Ciudad', max_length=35)

    def __str__(self):
        return "%s %s %s %s" % (self.zip_idzipco, self.zip_country, self.zip_estddet, self.zip_ciuddet)


class Aspirante(models.Model):
    asp_frsname = models.CharField('Primer Nombre', max_length=15)
    asp_midname = models.CharField('Segundo Nombre', max_length=15)
    asp_secmanp = models.CharField('Apellidos', max_length=25)
    asp_secmanm = models.CharField('Apellidos', max_length=25)
    asp_fechnac = models.DateField('Fecha de Nacimiento')
    asp_direcci = models.CharField('Direccion Domiciliaria', max_length=50)
    asp_zipcodg = models.ForeignKey(Zipcodigo, null=True, blank=True)
    asp_telefon = models.CharField('Telefono', max_length=15, blank=True)
    asp_celular = models.CharField('Celular', max_length=15, blank=True)
    asp_correoe = models.EmailField('e-mail')
    asp_imgclte = models.ImageField(upload_to="clientes", blank=True)
    asp_rgunico = models.CharField('Registro Unico', max_length=20, blank=True)
    asp_categor = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s %s" % (self.asp_frsnameo, self.asp_midname, self.asp_secmanp, self.asp_secmanm)


class Evento(models.Model):
    evn_fechaev = models.DateField('Fecha deEvento')
    evn_zipcode = models.ForeignKey(Zipcodigo)
    evn_direcci = models.TextField('Dirección', max_length=75)
    evn_localid = models.TextField('Local', max_length=50)
    evn_asisten = models.IntegerField('Cantida de asistentes')
    evn_pendien = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s %s %s" % (self.evn_fechaev, self.evn_zipcode, self.evn_direcci, self.evn_localid)


class Mensaje(models.Model):
    eml_fechmsj = models.DateField('Fecha de Mensaje')
    eml_descrip = models.EmailField('email')
    eml_mensaje = models.TextField('Mensaje')
    eml_requier = models.BooleanField(default=False)
    eml_aspiran = models.ForeignKey(Aspirante)

    def __str__(self):
        return self.eml_descrip
