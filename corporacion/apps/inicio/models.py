from django.db import models
from django.utils import timezone


class Contacto(models.Model):
    cnt_frsname = models.CharField('Primer Nombre', max_length=25)
    cnt_lasname = models.CharField('Apellidos', max_length=25)
    cnt_telefon = models.CharField('Núm. de teléfono', max_length=50)
    cnt_correoe = models.EmailField('e-mail')
    cnt_fechmsj = models.DateField('Fecha de Mensaje', default=timezone.now)
    cnt_mensaje = models.CharField('Mensaje', max_length=250)

    def __str__(self):
        return self.cnt_correoe
