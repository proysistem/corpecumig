from django import forms
from apps.eventos.models import Zipcodigo, Aspirante, Asistente, Evento, Mensaje
from django.utils.timezone import localtime, now


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
    eml_fechmsj = forms.DateTimeField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )

    class Meta:
        model = Mensaje

        fields = [
                # 'eml_fechmsj',
                'eml_descrip',
                'eml_mensaje',
                'eml_requier',
                'eml_aspiran',
                ]
        labels = {
                # 'eml_fechmsj': '',
                'eml_descrip': '',
                'eml_mensaje': '',
                'eml_requier': '',
                'eml_aspiran': '',
                }
        widgets = {
                # 'eml_fechmsj': forms.TextInput(),
                'eml_descrip': forms.TextInput(),
                'eml_mensaje': forms.TextInput(),
                'eml_requier': forms.TextInput(),
                'eml_aspiran': forms.TextInput(),
                }


class EventoForm(forms.ModelForm):
    evn_fechaev = forms.DateTimeField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )

    class Meta:
        model = Evento

        fields = [
                # 'evn_fechaev',
                'evn_horaevn',
                'evn_zipcode',
                'evn_direcci',
                'evn_localid',
                'evn_asisten',
                'evn_pendien',
                ]
        labels = {
                # 'evn_fechaev': 'Fecha del evento',
                'evn_horaevn': 'Hora del evento',
                'evn_zipcode': 'Lugar (zip-code)',
                'evn_direcci': 'Dirección',
                'evn_localid': 'Local',
                'evn_asisten': 'Asistentes, default=0',
                'evn_pendien': 'Pendiente(si/no)',
                }
        widgets = {
                # 'evn_fechaev': forms.DateInput(),
                'evn_horaevn': forms.TimeInput(),
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


class AsistenteForm(forms.ModelForm):

    class Meta:
        model = Asistente

        fields = [
                'ast_frsname',
                'ast_lasname',
                'ast_direcci',
                'ast_zipcodg',
                'ast_celular',
                'ast_correoe',
                'ast_categor',
                ]
        labels = {
                'ast_frsname': 'Nombre',
                'ast_lasname': 'Apellido',
                'ast_direcci': 'Dirección',
                'ast_zipcodg': 'Zip-código',
                'ast_celular': 'Celular',
                'ast_correoe': 'E-mail',
                'ast_categor': 'Status (0/1)',
                }
        widgets = {
                'ast_frsname': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'ast_lasname': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'ast_direcci': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'ast_zipcodg': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'ast_celular': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'ast_correoe': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                'ast_categor': forms.TextInput(attrs={"class": "form_input", "autocomplete": "off"}),
                 }
