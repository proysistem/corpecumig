from django import forms
from .models import Imagen, Socio, Cosocio
from django.utils.timezone import localtime, now


class ImagenForm(forms.ModelForm):
    img_fechreg = forms.DateField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )

    class Meta:
        model = Imagen

        fields = [
                 'img_corresp',
                 'img_nombres',
                 'img_detalle',
                 'img_imagenx',
                 'img_fechreg',
                 ]

        labels = {
                 'img_corresp':  'First Name',
                 'img_nombres':  'Last Name',
                 'img_detalle':  'Phone',
                 'img_imagenx':  'E-mail',
                 'img_fechreg':  'Date (mm/dd/yyyy)',
                 }

        widgets = {
                 'img_corresp': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'img_nombres': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'img_detalle': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'img_imagenx': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'img_fechreg': forms.DateInput(),
                }


class SocioForm(forms.ModelForm):
    soc_fechreg = forms.DateField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )

    soc_fechnac = forms.DateField(
        initial=localtime(now()).date(),
        label='Fecha de Nacimiento (mm/dd/yy)',
        widget=forms.DateInput(attrs={'class': 'form_input', 'type': 'date'}, format='%Y-%m-%d',)
    )

    soc_cosocio = forms.TypedChoiceField(
                   coerce=lambda x: x == 'Si',
                   choices=((False, 'No'), (True, 'Si')),
                   label='Registrar conyugue o Co-Soci@',
                   widget=forms.RadioSelect
    )

    class Meta:
        model = Socio

        fields = [
                'soc_nombres',
                'soc_apellid',
                'soc_fechnac',
                'soc_identif',
                'soc_direcci',
                'soc_citynam',
                'soc_statnam',
                'soc_paisnam',
                'soc_zipcodg',
                'soc_telefon',
                'soc_celular',
                'soc_correoe',
                'soc_imgfoto',
                'soc_imgidea',
                'soc_imgideb',
                'soc_rgunico',
                'soc_registr',
                'soc_accions',
                'soc_cosocio',
                'soc_categor',
                ]
        labels = {
                'soc_nombres': 'Nombres  ',
                'soc_apellid': 'Apellidos',
                'soc_fechnac': 'Fecha/Nacimiento (dd/mm/aa)',
                'soc_identif': 'Núm. de Identificación',
                'soc_direcci': 'Dirección    ',
                'soc_citynam': 'Ciudad',
                'soc_statnam': 'Estado o Provincia',
                'soc_paisnam': 'País',
                'soc_zipcodg': 'Código postal',
                'soc_telefon': 'Telef.de casa',
                'soc_celular': 'Núm. /celular',
                'soc_correoe': 'Correo electrónico',
                'soc_imgfoto': 'Foto de Socio',
                'soc_imgidea': 'Imagen del Id. lado(A)',
                'soc_imgideb': 'Imagen del Id. lado(B)',
                'soc_rgunico': 'Regist. Unico',
                'soc_registr': 'Acionista registrado',
                'soc_cosocio': 'Quiere adherir a alguien',
                'soc_accions': 'Cantidad de Aciones',
                # 'soc_categor': 'Categoría    ',
                }
        widgets = {
                'soc_nombres': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off', 'size': '30'}),
                'soc_apellid': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                # 'soc_fechnac': forms.DateInput(attrs={'class': 'form_input', 'type': 'date'}),
                # 'soc_fechnac': forms.DateInput(attrs={'class': 'form_input', 'type': 'date'}, format={'%Y-%m-%d'}),
                'soc_identif': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off', 'size': '15'}),
                'soc_direcci': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_citynam': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_statnam': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_paisnam': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_zipcodg': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_telefon': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_celular': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_correoe': forms.EmailInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_imgfoto': forms.ClearableFileInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_imgidea': forms.ClearableFileInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_imgideb': forms.ClearableFileInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_rgunico': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_registr': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_accions': forms.NumberInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                # 'soc_cosocio': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'soc_categor': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                }


class CosocioForm(forms.ModelForm):
    cso_fechreg = forms.DateField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )

    cso_fechnac = forms.DateField(
        initial=localtime(now()).date(),
        label='Fecha de Nacimiento (mm/dd/yy)',
        widget=forms.DateInput(attrs={'class': 'form_input', 'type': 'date'}, format='%Y-%m-%d',)
    )

    class Meta:
        model = Cosocio

        fields = [
                'cso_idsocio',
                'cso_nombres',
                'cso_apellid',
                'cso_fechnac',
                'cso_identif',
                'cso_direcci',
                'cso_citynam',
                'cso_statnam',
                'cso_paisnam',
                'cso_zipcodg',
                'cso_telefon',
                'cso_celular',
                'cso_correoe',
                'cso_imgfoto',
                'cso_imgidea',
                'cso_imgideb',
                'cso_rgunico',
                'cso_registr',
                'cso_accions',
                'cso_categor',
                ]
        labels = {
                # 'cso_idsocio': ''
                'cso_nombres': 'Nombres  ',
                'cso_apellid': 'Apellidos',
                'cso_fechnac': 'Fecha/Nacimiento (dd/mm/aa)',
                'cso_identif': 'Núm. de Identificación',
                'cso_direcci': 'Dirección',
                'cso_citynam': 'Ciudad',
                'cso_statnam': 'Estado o Provincia',
                'cso_paisnam': 'País',
                'cso_zipcodg': 'Código postal',
                'cso_telefon': 'Telef.de casa',
                'cso_celular': 'Núm. /celular',
                'cso_correoe': 'Correo electrónico',
                'cso_imgfoto': 'Foto de Socio',
                'cso_imgidea': 'Imagen del Id. lado(A)',
                'cso_imgideb': 'Imagen del Id. lado(B)',
                'cso_rgunico': 'Regist. Unico',
                'cso_registr': 'Acionista registrado',
                'cso_accions': 'Cantidad de Aciones',
                # 'cso_categor': 'Categoría    ',
                }
        widgets = {
                # 'cso_idsocio'
                'cso_nombres': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off', 'size': '30'}),
                'cso_apellid': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_fechnac': forms.DateInput(attrs={'class': 'form_input', 'type': 'date'}),
                'cso_identif': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off', 'size': '15'}),
                'cso_direcci': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_citynam': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_statnam': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_paisnam': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_zipcodg': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_telefon': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_celular': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_correoe': forms.EmailInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_imgfoto': forms.ClearableFileInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_imgidea': forms.ClearableFileInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_imgideb': forms.ClearableFileInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_rgunico': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_registr': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                'cso_accions': forms.NumberInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                # 'cso_categor': forms.TextInput(attrs={'class': 'form_input', 'autocomplete': 'off'}),
                 }
