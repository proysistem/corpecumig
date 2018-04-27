from django.db import models


class Contacto(models.Model):
    cnt_frsname = models.CharField('Primer Nombre', max_length=25)
    cnt_lasname = models.CharField('Apellidos', max_length=25)
    cnt_telefon = models.CharField('Núm. de teléfono', max_length=50)
    cnt_correoe = models.EmailField('e-mail')
    cnt_fechmsj = models.DateTimeField(auto_now_add=True, editable=False)
    cnt_mensaje = models.CharField('Mensaje', max_length=250)

    def __str__(self):
        return self.cnt_correoe


class Solicitud(models.Model):
    req_frsname = models.CharField('Primer Nombre', max_length=15)
    req_secname = models.CharField('Apellidos', max_length=25)
    req_direcci = models.CharField('Dirección Domiciliaria', max_length=50)
    req_zipcodg = models.CharField('Código postal', null=True, blank=True, max_length=10)
    req_correoe = models.EmailField('e-mail')
    req_fechmsj = models.DateTimeField(auto_now_add=True, editable=False)
    req_descrip = models.TextField('Titulo', max_length=25, default='Solicito exposición')
    req_mensaje = models.CharField('Mensaje', max_length=220)
    req_requier = models.BooleanField(default=True)

    def __str__(self):
        return self.req_zipcodg


class Aspirante(models.Model):
    asp_nombres = models.CharField('Primer Nombre', max_length=25)
    asp_apellid = models.CharField('Apellidos', max_length=25)
    asp_fechnac = models.DateField('Fecha de Nacimiento')
    asp_direcci = models.CharField('Direccion Domiciliaria', max_length=50)
    asp_zipcodg = models.CharField('Cód. Postal', max_length=15, null=True, blank=True)
    asp_telefon = models.CharField('Telefono', max_length=15, blank=True)
    asp_celular = models.CharField('Celular', max_length=15, blank=True)
    asp_correoe = models.EmailField('e-mail')
    asp_imgclte = models.ImageField(upload_to="clientes", blank=True)
    asp_rgunico = models.CharField('Registro Unico', max_length=20, blank=True)
    asp_categor = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.asp_nombres, self.asp_apellid)
