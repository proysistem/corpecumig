from django.db import models


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
