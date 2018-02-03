from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .forms import ZipcodigoForm, MensajeForm, EventoForm, AspiranteForm

from apps.eventos.models import Zipcodigo, Aspirante, Evento, Mensaje

# ========Z  I  P  C  O  D  I  G  O  =========== #


class ZipLista(ListView):
    """Listado de Zipcodigo"""
    model = Zipcodigo
    template_name = 'eventos/Zip_Panel.html'
    ordering = ['pk']
    paginate_by = 15


class ZipView(DetailView):
    """Listado de Zipcodigo"""
    template_name = 'eventos/Zip_View.html'
    model = Zipcodigo


class ZipNuevo(CreateView):
    """Crear Zipcodigo"""
    model = Zipcodigo
    form_class = ZipcodigoForm
    template_name = 'eventos/Zip_New.html'
    success_url = reverse_lazy('eventos:zip_panel')


class ZipEdita(UpdateView):
    """Listado de Zipcodigos"""
    model = Zipcodigo
    form_class = ZipcodigoForm
    template_name = 'eventos/Zip_Edit.html'
    success_url = reverse_lazy('eventos:zip_panel')


class ZipDelet(DeleteView):
    """Listado de Zipcodigos"""
    model = Zipcodigo
    form_class = ZipcodigoForm
    template_name = 'eventos/Zip_Delet.html'
    success_url = reverse_lazy('eventos:zip_panel')


# ======== M  E  N  S  A  J  E  =========== #


class MsgLista(ListView):
    """Listado de Mensaje"""
    model = Mensaje
    template_name = 'eventos/Msg_Panel.html'
    ordering = ['pk']
    paginate_by = 15


class MsgView(DetailView):
    """Listado de Mensaje"""
    template_name = 'eventos/Msg_View.html'
    model = Mensaje


class MsgNuevo(CreateView):
    """Crear Mensaje"""
    model = Mensaje
    form_class = MensajeForm
    template_name = 'eventos/Msg_New.html'
    success_url = reverse_lazy('eventos:msg_panel')


class MsgEdita(UpdateView):
    """Listado de Mensajes"""
    model = Mensaje
    form_class = MensajeForm
    template_name = 'eventos/Msg_Edit.html'
    success_url = reverse_lazy('eventos:msg_panel')


class MsgDelet(DeleteView):
    """Listado de Mensajes"""
    model = Mensaje
    form_class = MensajeForm
    template_name = 'eventos/Msg_Delet.html'
    success_url = reverse_lazy('eventos:msg_panel')

# ========  E  V  E  N  T  O  S  =========== #


class EvnLista(ListView):
    """Listado de Evento"""
    model = Evento
    template_name = 'eventos/Evn_Panel.html'
    ordering = ['pk']
    paginate_by = 15


class EvnView(DetailView):
    """Listado de Evento"""
    template_name = 'eventos/Evn_View.html'
    model = Evento


class EvnNuevo(CreateView):
    """Crear Evento"""
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/Evn_New.html'
    success_url = reverse_lazy('eventos:evn_panel')


class EvnEdita(UpdateView):
    """Listado de Eventos"""
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/Evn_Edit.html'
    success_url = reverse_lazy('eventos:evn_panel')


class EvnDelet(DeleteView):
    """Listado de Eventos"""
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/Evn_Delet.html'
    success_url = reverse_lazy('eventos:evn_panel')

# ========  A  S  P  I  R  A  N  T  E  S  =========== #


class AspLista(ListView):
    """Listado de Aspirante"""
    model = Aspirante
    template_name = 'eventos/Asp_Panel.html'
    ordering = ['pk']
    paginate_by = 15


class AspView(DetailView):
    """Listado de Aspirante"""
    template_name = 'eventos/Asp_View.html'
    model = Aspirante


class AspNuevo(CreateView):
    """Crear Aspirante"""
    model = Aspirante
    form_class = AspiranteForm
    template_name = 'eventos/Asp_New.html'
    success_url = reverse_lazy('eventos:asp_panel')


class AspEdita(UpdateView):
    """Listado de Aspirantes"""
    model = Aspirante
    form_class = AspiranteForm
    template_name = 'eventos/Asp_Edit.html'
    success_url = reverse_lazy('eventos:asp_panel')


class AspDelet(DeleteView):
    """Listado de Aspirantes"""
    model = Aspirante
    form_class = AspiranteForm
    template_name = 'eventos/Asp_Delet.html'
    success_url = reverse_lazy('eventos:asp_panel')
