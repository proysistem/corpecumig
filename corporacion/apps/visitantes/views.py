from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView
from apps.eventos.forms import MensajeForm, AspiranteForm
from apps.eventos.models import Aspirante, Evento, Mensaje
from .models import Solicitud
from .forms import SolicitudForm

# ========  E  V  E  N  T  O  S  =========== #


class Evn_Lista(ListView):
    """Listado de Evento"""
    model = Evento
    template_name = 'visitantes/Evn_Panel.html'
    ordering = ['pk']
    paginate_by = 15

# ========  A  S  P  I  R  A  N  T  E  S  =========== #


class Sol_Nuevo(CreateView):
    """Crear Aspirante"""
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'visitantes/Sol_New.html'
    success_url = reverse_lazy('inicio:home')

# ========  A  S  P  I  R  A  N  T  E  S  =========== #


class Asp_Nuevo(CreateView):
    """Crear Aspirante"""
    model = Aspirante
    form_class = AspiranteForm
    template_name = 'visitantes/Asp_New.html'
    success_url = reverse_lazy('inicio:home')

# ======== M  E  N  S  A  J  E  =========== #


class Msg_Nuevo(CreateView):
    """Crear Mensaje"""
    model = Mensaje
    form_class = MensajeForm
    template_name = 'visitantes/Msg_New.html'
    success_url = reverse_lazy('visitantes:msg_panel')
