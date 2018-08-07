from django.db import models


class Socio(models.Model):
    soc_nombres = models.CharField('Primer Nombre', max_length=25)
    soc_apellid = models.CharField('Apellidos', max_length=30)
    soc_fechnac = models.DateField('Fecha de Nacimiento')
    soc_identif = models.CharField('Id. del socio', unique=True,  db_index=True, max_length=15)
    soc_direcci = models.CharField('Direccion Domiciliaria', max_length=50)
    soc_citynam = models.CharField('Ciudad', max_length=30, null=True, blank=True)
    soc_statnam = models.CharField('Estado / Porvincia', max_length=30, null=True, blank=True)
    soc_paisnam = models.CharField('País', max_length=30, null=True, blank=True)
    soc_zipcodg = models.CharField('Cód. Postal', max_length=15, null=True, blank=True)
    soc_telefon = models.CharField('Telefono', max_length=15, null=True, blank=True)
    soc_celular = models.CharField('Celular', max_length=15, null=True, blank=True)
    soc_correoe = models.EmailField('e-mail',  max_length=75, null=True, blank=True)
    soc_imgfoto = models.ImageField(upload_to="socio", null=True, blank=True)
    soc_imgidea = models.ImageField(upload_to="socio", null=True, blank=True)
    soc_imgideb = models.ImageField(upload_to="socio", null=True, blank=True)
    soc_rgunico = models.CharField('Registro Unico', max_length=20, blank=True)
    soc_registr = models.CharField(default='No', max_length=3,  null=True, blank=True)
    soc_accions = models.PositiveIntegerField()
    soc_fechreg = models.DateField('Fecha de registración', auto_now_add=True, editable=False)
    soc_categor = models.CharField(default='0', max_length=3, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.soc_nombres, self.soc_apellid)


class Imagen(models.Model):
    img_corresp = models.ForeignKey(Socio, null=True, blank=True)
    img_nombres = models.CharField('Nombre de la imagen', max_length=30)
    img_detalle = models.CharField('Detalle de la imagen', max_length=75)
    img_imagenx = models.ImageField(upload_to="clientes", blank=True)
    img_fechreg = models.DateField('Fecha de registración')

    def __str__(self):
        return "%s %s" % (self.img_detalle, self.img_imagenx)
