from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Socio, Cosocio
from .forms import SocioForm, CosocioForm

# ========  s o c i o s  =========== #


class Soc_Panel(ListView):
    """Listado de Socio"""
    model = Socio
    template_name = 'socios/Soc_Panel.html'
    paginate_by = 15


class Soc_Nuevo(CreateView):
    """Crear Socio"""
    model = Socio
    form_class = SocioForm
    template_name = 'socios/Soc_New.html'
    success_url = reverse_lazy('inicio:iniciar')


class Soc_View(DetailView):
    """Listado de Socio"""
    template_name = 'socios/Soc_View.html'
    model = Socio


class Soc_Edita(UpdateView):
    """Listado de Socios"""
    model = Socio
    form_class = SocioForm
    template_name = 'socios/Soc_Edit.html'
    success_url = reverse_lazy('socios:soc_panel')


class Soc_Delet(DeleteView):
    """Listado de Socios"""
    model = Socio
    form_class = SocioForm
    template_name = 'socios/Soc_Delet.html'
    success_url = reverse_lazy('socios:soc_panel')


# class Pop_Opcion(request):

    # template = 'socios/Pop_Opcion.html'
    # return render(request, template, context)


class Cso_Panel(ListView):
    """Listado de Cosocio"""
    model = Cosocio
    form_class = CosocioForm
    template_name = 'socios/Cso_Panel.html'
    ordering = ['pk']
    paginate_by = 15


class Cso_Nuevo(CreateView):
    """Crear Cosocio"""
    model = Cosocio
    form_class = CosocioForm
    template_name = 'socios/Cso_New.html'
    success_url = reverse_lazy('inicio:iniciar')


class Cso_View(DetailView):
    """Listado de Cosocio"""
    template_name = 'socios/Cso_View.html'
    model = Cosocio


class Cso_Edita(UpdateView):
    """Listado de Cosocios"""
    model = Cosocio
    form_class = CosocioForm
    template_name = 'socios/Cso_Edit.html'
    success_url = reverse_lazy('socios:cso_panel')


class Cso_Delet(DeleteView):
    """Listado de Cosocios"""
    model = Cosocio
    form_class = CosocioForm
    template_name = 'socios/Cso_Delet.html'
    success_url = reverse_lazy('socios:cso_panel')


# class Pop_Opcion(request):

    # template = 'socios/Pop_Opcion.html'
    # return render(request, template, context)


def Pop_Opcion(request):

    # context = {}
    template = 'socios/Pop_Opcion.html'
    return render(request, template)
