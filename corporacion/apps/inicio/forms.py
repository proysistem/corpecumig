from django import forms
from .models import Contacto
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
