from django.shortcuts import render
from django.views.generic import CreateView, ListView
from apps.eventos.models import Evento
from django.core.urlresolvers import reverse_lazy
from .models import Contacto, Aspirante, Solicitud

from .forms import ContactoForm, AspiranteForm, SolicitudForm


def IndexView(request):

    context = {}
    template = 'inicio/index.html'
    return render(request, template, context)


def nosotros(request):

    context = {}
    template = 'inicio/nosotros.html'
    return render(request, template, context)


class proyecto(ListView):
    """Listado de Eventos"""
    model = Evento
    template_name = 'inicio/proyecto.html'
    ordering = ['pk']
    paginate_by = 15
    success_url = reverse_lazy('inicio:iniciar')


def propuesta(request):

    context = {}
    template = 'inicio/propuesta.html'
    return render(request, template, context)


class Acc_Panel(ListView):
    """Listado de Eventos"""
    template_name = 'inicio/Acc_Panel.html'

# ========  C  O  N  T  A  C  T  O  =========== #


class Cnt_Nuevo(CreateView):
    """Crear un Contacto """
    model = Contacto
    form_class = ContactoForm
    template_name = 'inicio/Cnt_New.html'
    success_url = reverse_lazy('inicio:contacto')

# ========  R E G I S T R O  =========== #


class Reg_Nuevo(CreateView):
    """Crear un Aspirante """
    model = Aspirante
    form_class = AspiranteForm
    template_name = 'inicio/Asp_New.html'
    success_url = reverse_lazy('inicio:contacto')

# ========  A  S  P  I  R  A  N  T  E  S  =========== #


class AspLista(ListView):
    """Listado de Aspirante"""
    model = Aspirante
    template_name = 'eventos/Asp_Panel.html'
    ordering = ['pk']
    paginate_by = 15

# ========  A  S  P  I  R  A  N  T  E  S  =========== #


# class Asp_Nuevo(CreateView):
#     """Crear Aspirante"""
#     model = Aspirante
#     form_class = AspiranteForm
#     template_name = 'visitantes/Asp_New.html'
#     success_url = reverse_lazy('inicio:iniciar')

# class AspView(DetailView):
#     """Listado de Aspirante"""
#     template_name = 'eventos/Asp_View.html'
#     model = Aspirante


# class AspNuevo(CreateView):
#     """Crear Aspirante"""
#     model = Aspirante
#     form_class = AspiranteForm
#     template_name = 'eventos/Asp_New.html'
#     success_url = reverse_lazy('eventos:asp_panel')


# class AspEdita(UpdateView):
#     """Listado de Aspirantes"""
#     model = Aspirante
#     form_class = AspiranteForm
#     template_name = 'eventos/Asp_Edit.html'
#     success_url = reverse_lazy('eventos:asp_panel')


# class AspDelet(DeleteView):
#     """Listado de Aspirantes"""
#     model = Aspirante
#     form_class = AspiranteForm
#     template_name = 'eventos/Asp_Delet.html'
#     success_url = reverse_lazy('eventos:asp_panel')


# ========  r E Q U I E R E  =========== #


class Req_Nuevo(CreateView):
    """Crear un Solicitud """
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'inicio/Sol_New.html'
    success_url = reverse_lazy('inicio:contacto')
