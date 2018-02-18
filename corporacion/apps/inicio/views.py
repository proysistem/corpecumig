from django.shortcuts import render
from django.views.generic import CreateView, ListView
from apps.eventos.models import Evento
from django.core.urlresolvers import reverse_lazy
from apps.visitantes.models import Contacto
from apps.visitantes.forms import ContactoForm
#    template_name = 'inicio/index.html'
#    config = None


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


# ========  C  O  N  T  A  C  T  O  =========== #


class Cnt_Nuevo(CreateView):
    """Crear un Contacto """
    model = Contacto
    form_class = ContactoForm
    template_name = 'inicio/Cnt_New.html'
    success_url = reverse_lazy('inicio:contacto')
