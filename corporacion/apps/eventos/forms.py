from django import forms
from apps.eventos.models import Zipcodigo, Aspirante, Evento, Mensaje


class ZipcodigoForm(forms.ModelForm):

    class Meta:
        model = Zipcodigo

        fields = [
                'zip_idzipco',
                'zip_country',
                'zip_estddet',
                'zip_estdabr',
                'zip_condado',
                'zip_ciuddet',
                 ]

        labels = {
                'zip_idzipco': '',
                'zip_country': '',
                'zip_estddet': '',
                'zip_estdabr': '',
                'zip_condado': '',
                'zip_ciuddet': '',
                 }

        widgets = {
                'zip_idzipco': forms.TextInput(),
                'zip_country': forms.TextInput(),
                'zip_estddet': forms.TextInput(),
                'zip_estdabr': forms.TextInput(),
                'zip_condado': forms.TextInput(),
                'zip_ciuddet': forms.TextInput(),
                }


class MensajeForm(forms.ModelForm):

    class Meta:
        model = Mensaje

        fields = [
                'eml_fechmsj',
                'eml_descrip',
                'eml_mensaje',
                'eml_requier',
                'eml_aspiran',
                ]
        labels = {
                'eml_fechmsj': '',
                'eml_descrip': '',
                'eml_mensaje': '',
                'eml_requier': '',
                'eml_aspiran': '',
                }
        widgets = {
                'eml_fechmsj': forms.TextInput(),
                'eml_descrip': forms.TextInput(),
                'eml_mensaje': forms.TextInput(),
                'eml_requier': forms.TextInput(),
                'eml_aspiran': forms.TextInput(),
                }


class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento

        fields = [
                'evn_fechaev',
                'evn_zipcode',
                'evn_direcci',
                'evn_localid',
                'evn_asisten',
                'evn_pendien',
                ]
        labels = {
                'evn_fechaev': '',
                'evn_zipcode': '',
                'evn_direcci': '',
                'evn_localid': '',
                'evn_asisten': '',
                'evn_pendien': '',
                }
        widgets = {
                'evn_fechaev': forms.TextInput(),
                'evn_zipcode': forms.TextInput(),
                'evn_direcci': forms.TextInput(),
                'evn_localid': forms.TextInput(),
                'evn_asisten': forms.TextInput(),
                'evn_pendien': forms.TextInput(),
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
