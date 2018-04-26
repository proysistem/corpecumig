from django.db import models


class Zipcodigo(models.Model):
    zip_idzipco = models.CharField("Código Postal", max_length=15, primary_key=True)
    zip_country = models.TextField('Pais', max_length=5)
    zip_estddet = models.TextField('Estado', max_length=30)
    zip_estdabr = models.TextField('Estado', max_length=5)
    zip_condado = models.TextField('Condado', max_length=35)
    zip_ciuddet = models.TextField('Ciudad', max_length=35)

    def __str__(self):
        return "%s %s %s %s" % (self.zip_country, self.zip_ciuddet, self.zip_estddet, self.zip_idzipco)


class Asistente(models.Model):
    ast_frsname = models.CharField('Primer Nombre', max_length=25)
    ast_lasname = models.CharField('Segundo Nombre', max_length=25)
    ast_direcci = models.CharField('Direccion Domiciliaria', max_length=50)
    ast_zipcodg = models.ForeignKey(Zipcodigo, null=True, blank=True)
    ast_celular = models.CharField('Celular', max_length=15, blank=True)
    ast_correoe = models.EmailField('e-mail')
    ast_categor = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.ast_frsname, self.ast_lasname)


class Evento(models.Model):
    evn_fechaev = models.DateTimeField(auto_now_add=True, editable=False)
    evn_horaevn = models.TimeField('Hora del evento')
    evn_zipcode = models.ForeignKey(Zipcodigo)
    evn_direcci = models.TextField('Dirección', max_length=75)
    evn_localid = models.TextField('Local', max_length=50)
    evn_asisten = models.IntegerField('Cantida de asistentes')
    evn_pendien = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s %s %s" % (self.evn_fechaev, self.evn_zipcode, self.evn_direcci, self.evn_localid)


class Mensaje(models.Model):
    eml_fechmsj = models.DateTimeField(auto_now_add=True, editable=False)
    eml_descrip = models.EmailField('email')
    eml_mensaje = models.TextField('Mensaje')
    eml_requier = models.BooleanField(default=False)
    # eml_aspiran = models.ForeignKey(Aspirante)

    def __str__(self):
        return self.eml_descrip
