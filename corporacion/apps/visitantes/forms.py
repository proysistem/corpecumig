from django import forms
from .models import Solicitud


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
