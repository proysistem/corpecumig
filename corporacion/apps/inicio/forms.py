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
                'asp_frsname',
                'asp_midname',
                'asp_secmanp',
                'asp_secmanm',
                'asp_fechnac',
                'asp_direcci',
                'asp_zipcodg',
                'asp_telefon',
                'asp_celular',
                'asp_correoe',
                'asp_imgclte',
                'asp_rgunico',
                'asp_categor',
                ]
        labels = {
                'asp_frsname': '',
                'asp_midname': '',
                'asp_secmanp': '',
                'asp_secmanm': '',
                'asp_fechnac': '',
                'asp_direcci': '',
                'asp_zipcodg': '',
                'asp_telefon': '',
                'asp_celular': '',
                'asp_correoe': '',
                'asp_imgclte': '',
                'asp_rgunico': '',
                'asp_categor': '',
                }
        widgets = {
                'asp_frsname': forms.TextInput(),
                'asp_midname': forms.TextInput(),
                'asp_secmanp': forms.TextInput(),
                'asp_secmanm': forms.TextInput(),
                'asp_fechnac': forms.TextInput(),
                'asp_direcci': forms.TextInput(),
                'asp_zipcodg': forms.TextInput(),
                'asp_telefon': forms.TextInput(),
                'asp_celular': forms.TextInput(),
                'asp_correoe': forms.TextInput(),
                'asp_imgclte': forms.TextInput(),
                'asp_rgunico': forms.TextInput(),
                'asp_categor': forms.TextInput(),
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
                 # 'req_fechmsj':  'Fecha (mm/dd/yyyy)',
                 # 'req_descrip':  'Descipción',
                 'req_mensaje':  'Mensaje',
                 }

        widgets = {
                 'req_frsname': forms.TextInput(),
                 'req_secname': forms.TextInput(),
                 'req_direcci': forms.TextInput(),
                 'req_zipcodg': forms.TextInput(),
                 'req_correoe': forms.TextInput(),
                 # 'req_fechmsj': forms.DateInput(),
                 # 'req_descrip': forms.TextInput(),
                 'req_mensaje': forms.Textarea(),
                }
