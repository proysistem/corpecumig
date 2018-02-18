from django import forms
from .models import Solicitud, Contacto


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
                 'req_frsname',
                 'req_secname',
                 'req_direcci',
                 'req_zipcodg',
                 'req_correoe',
                 'req_fechmsj',
                 # 'req_descrip',
                 'req_mensaje',
                 # 'req_requier',
                 ]

        labels = {
                 'req_frsname':  'Nombres',
                 'req_secname':  'Apellidos',
                 'req_direcci':  'Dirección',
                 'req_zipcodg':  'Zip-código',
                 'req_correoe':  'E-mail',
                 'req_fechmsj':  'Fecha (mm/dd/yyyy)',
                 # 'req_descrip':  'Descipción',
                 'req_mensaje':  'Mensaje',
                 }

        widgets = {
                 'req_frsname': forms.TextInput(),
                 'req_secname': forms.TextInput(),
                 'req_direcci': forms.TextInput(),
                 'req_zipcodg': forms.TextInput(),
                 'req_correoe': forms.TextInput(),
                 'req_fechmsj': forms.DateInput(),
                 # 'req_descrip': forms.TextInput(),
                 'req_mensaje': forms.Textarea(),
                }


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto

        fields = [
                 'cnt_frsname',
                 'cnt_lasname',
                 'cnt_telefon',
                 'cnt_correoe',
                 'cnt_fechmsj',
                 'cnt_mensaje',
                 ]

        labels = {
                 'cnt_frsname':  'First Name',
                 'cnt_lasname':  'Last Name',
                 'cnt_telefon':  'Phone',
                 'cnt_correoe':  'E-mail',
                 'cnt_fechmsj':  'Date (mm/dd/yyyy)',
                 'cnt_mensaje':  'Message',
                 }

        widgets = {
                 'cnt_frsname': forms.TextInput(attrs={"class": "form_input"}),
                 'cnt_lasname': forms.TextInput(attrs={"class": "form_input"}),
                 'cnt_telefon': forms.TextInput(attrs={"class": "form_input"}),
                 'cnt_correoe': forms.TextInput(attrs={"class": "form_input"}),
                 'cnt_fechmsj': forms.DateInput(),
                 'cnt_mensaje': forms.Textarea(attrs={"class": "form_textarea"}),
                }
