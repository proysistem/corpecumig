from django import forms
from .models import Contacto, Aspirante, Solicitud
from django.utils.timezone import localtime, now


class ContactoForm(forms.ModelForm):
    cnt_fechmsj = forms.DateField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )

    class Meta:
        model = Contacto

        fields = [
                 'cnt_frsname',
                 'cnt_lasname',
                 'cnt_telefon',
                 'cnt_correoe',
                 # 'cnt_fechmsj',
                 'cnt_mensaje',
                 ]

        labels = {
                 'cnt_frsname':  'First Name',
                 'cnt_lasname':  'Last Name',
                 'cnt_telefon':  'Phone',
                 'cnt_correoe':  'E-mail',
                 # 'cnt_fechmsj':  'Date (mm/dd/yyyy)',
                 'cnt_mensaje':  'Message',
                 }

        widgets = {
                 'cnt_frsname': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'cnt_lasname': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'cnt_telefon': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'cnt_correoe': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 # 'cnt_fechmsj': forms.DateInput(),
                 'cnt_mensaje': forms.Textarea(attrs={"class": "form_textarea"}),
                }


class AspiranteForm(forms.ModelForm):

    class Meta:
        model = Aspirante

        fields = [
                'asp_nombres',
                'asp_apellid',
                'asp_fechnac',
                'asp_direcci',
                'asp_zipcodg',
                'asp_telefon',
                'asp_celular',
                'asp_correoe',
                'asp_imgclte',
                'asp_rgunico',
                # 'asp_categor',
                ]
        labels = {
                'asp_nombres': 'Nombres  ',
                'asp_apellid': 'Apellidos',
                'asp_fechnac': 'F./nacimiento (dd/mm/aa)',
                'asp_direcci': 'Dirección    ',
                'asp_zipcodg': 'Código postal',
                'asp_telefon': 'Telef.de casa',
                'asp_celular': 'Núm. /celular',
                'asp_correoe': 'Correo electrónico',
                'asp_imgclte': 'Fot.Aspirante',
                'asp_rgunico': 'Regist. Unico',
                # 'asp_categor': 'Categoría    ',
                }
        widgets = {
                'asp_nombres': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_apellid': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_fechnac': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_direcci': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_zipcodg': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_telefon': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_celular': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_correoe': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_imgclte': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'asp_rgunico': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                # 'asp_categor': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 }


class SolicitudForm(forms.ModelForm):
    req_fechmsj = forms.DateTimeField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )

    class Meta:
        model = Solicitud

        fields = [
                 'req_frsname',
                 'req_secname',
                 'req_direcci',
                 'req_zipcodg',
                 'req_correoe',
                 # 'req_fechmsj',
                 # 'req_descrip',
                 'req_mensaje',
                 ]

        labels = {
                 'req_frsname':  'Nombres',
                 'req_secname':  'Apellidos',
                 'req_direcci':  'Dirección',
                 'req_zipcodg':  'Zip-código',
                 'req_correoe':  'E-mail',
                 'req_fechmsj':  'Fecha mensaje',
                 # 'req_descrip':  'Descipción',
                 'req_mensaje':  'Mensaje',
                 }

        widgets = {
                 'req_frsname': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'req_secname': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'req_direcci': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'req_zipcodg': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'req_correoe': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 # 'req_fechmsj': forms.DateInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 # 'req_descrip': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 'req_mensaje': forms.Textarea(attrs={"class": "form_input", "autocomplete": "off"}),
                }
