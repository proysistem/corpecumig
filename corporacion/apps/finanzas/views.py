from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import Caja, Cajera, Movicaja, Plancuenta, Saldocontab, Comprobante
from .forms import CajaForm, CajeraForm, MovicajaForm, Plancuentaform, SaldocontabForm, ComprobanteForm
from django.http import Http404  # , HttpResponse


# ===================================================================================== #
# ------------------------- |   C A J E R A  | ---------------------------------------- #
# ===================================================================================== #


class Cjr_Lista(ListView):
    """Listado de Cajera"""
    model = Cajera
    template_name = 'finanzas/Cjr_Panel.html'
    ordering = ['pk']
    paginate_by = 15


class Cjr_Nuevo(CreateView):
        """Crear Cajera"""
        model = Cajera
        form_class = CajeraForm
        template_name = 'finanzas/Cjr_New.html'
        success_url = reverse_lazy('finanzas:cjr_panel')

        def form_invalid(self, form):
            messages.error(self.request, 'Hay un error en el formulario')
            return super(Cjr_Nuevo, self).form_invalid(form)


class Cjr_View(DetailView):
    """Visualiza Cajera"""
    template_name = 'finanzas/Cjr_View.html'
    model = Cajera
    form_class = CajeraForm


class Cjr_Edita(UpdateView):
    """Actualiza Cajeras"""
    model = Cajera
    form_class = CajeraForm
    template_name = 'finanzas/Cjr_Edit.html'
    success_url = reverse_lazy('finanzas:cjr_panel')


class Cjr_Delet(DeleteView):
    """Elimina Cajeras"""
    model = Cajera
    form_class = CajeraForm
    template_name = 'finanzas/Cjr_Delet.html'
    success_url = reverse_lazy('finanzas:cjr_panel')

# ===================================================================================== #
# --------------------------|  C   A   J   A |----------------------------------------- #
# ===================================================================================== #


class Cja_Lista(ListView):
    """Listado de Caja"""
    model = Caja
    template_name = 'finanzas/Cja_Panel.html'
    ordering = ['pk']
    paginate_by = 15


class Cja_Nuevo(CreateView):
        """Crear Caja"""
        model = Caja
        form_class = CajaForm
        template_name = 'finanzas/Cja_New.html'
        success_url = reverse_lazy('finanzas:cja_panel')

        def form_invalid(self, form):
            messages.error(self.request, 'Hay un error en el formulario')
            return super(Cja_Nuevo, self).form_invalid(form)


class Cja_View(DetailView):
    """Visualiza Caja"""
    template_name = 'finanzas/Cja_View.html'
    model = Caja
    form_class = CajaForm


class Cja_Edita(UpdateView):
    """Actualiza Cajas"""
    model = Caja
    form_class = CajaForm
    template_name = 'finanzas/Cja_Edit.html'
    success_url = reverse_lazy('finanzas:cja_panel')


class Cja_Delet(DeleteView):
    """Elimina Cajas"""
    model = Caja
    form_class = CajaForm
    template_name = 'finanzas/Cja_Delet.html'
    success_url = reverse_lazy('finanzas:cja_panel')

# ===================================================================================== #
# -----------------------| M O V I M I E N  T O   C A J A  |--------------------------- #
# ===================================================================================== #
# class Mja-Buscar(TemplateView):


class Mcj_Lista(ListView):
    """Listado de Caja"""
    model = Movicaja
    template_name = 'finanzas/Mja_Panel.html'
    ordering = ['pk']
    paginate_by = 15


class Mcj_Nuevo(CreateView):
    """Crear Movicaja"""
    model = Movicaja
    form_class = MovicajaForm
    template_name = 'finanzas/Mja_New.html'
    success_url = reverse_lazy('finanzas:mja_panel')

    def form_invalid(self, form):
        messages.error(self.request, 'Hay un error en el formulario')
        return super(Mcj_Nuevo, self).form_invalid(form)


class Mcj_View(DetailView):
    """Visualiza Movicaja"""
    template_name = 'finanzas/Mcj_View.html'
    model = Movicaja
    form_class = MovicajaForm


class Mcj_Edita(UpdateView):
    """Actualiza Movicajas"""
    model = Movicaja
    form_class = MovicajaForm
    template_name = 'finanzas/Mcj_Edit.html'
    success_url = reverse_lazy('finanzas:mcj_panel')


class Mcj_Delet(DeleteView):
    """Elimina Movicajas"""
    model = Movicaja
    form_class = MovicajaForm
    template_name = 'finanzas/Mcj_Delet.html'
    success_url = reverse_lazy('finanzas:mcj_panel')

# ===================================================================================== #
# ----------------------| P  L  A  N    DE   C  U  E  N  T  A  S |--------------------- #
# ===================================================================================== #
# class Plc_Buscar(TemplateView):


class Plc_Lista(ListView):
    """Listado de Plancuenta"""
    model = Plancuenta
    template_name = 'finanzas/Plc_Panel.html'
    ordering = ['pk']
    paginate_by = 18


class Plc_Nuevo(CreateView):
        """Crear Plancuentas"""
        model = Plancuenta
        form_class = Plancuentaform
        template_name = 'finanzas/Plc_New.html'
        success_url = reverse_lazy('finanzas:plc_panel')

        def form_invalid(self, form):
            messages.error(self.request, 'Hay un error en el formulario')
            return super(Plc_Nuevo, self).form_invalid(form)


class Plc_View(DetailView):
    """Visualiza Plancuenta"""
    template_name = 'finanzas/Plc_View.html'
    model = Plancuenta
    form_class = Plancuentaform


class Plc_Edita(UpdateView):
    """Actualiza Plancuentas"""
    model = Plancuenta
    form_class = Plancuentaform
    template_name = 'finanzas/Plc_Edit.html'
    success_url = reverse_lazy('finanzas:plc_panel')


class Plc_Delet(DeleteView):
    """Elimina Plancuentas"""
    model = Plancuenta
    form_class = Plancuentaform
    template_name = 'finanzas/Plc_Delet.html'
    success_url = reverse_lazy('finanzas:plc_panel')


class Plc_Query(DetailView):
    """Consulta de Plancta"""
    model = Plancuenta
    template_name = 'finanzas/Plc_Query.html'
    context_object_name = 'plancta'

    slug_field = 'plc_ncuenta'
    slug_url_kwarg = 'plc_ncuenta'
    pk_url_kwarg = None

    def get(self, request, *args, **kwargs):
        contexto = {}
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
            contexto['err_err404'] = True
            contexto['probado'] = 'probando'
        context = self.get_context_data(object=self.object)
        context.update(contexto)
        return self.render_to_response(context)


# ===================================================================================== #
# --------------------------| S A L D O S    C O N  T B L E S |------------------------ #
# ===================================================================================== #


class Slc_Lista(ListView):
    """Listado de Saldocontab"""
    model = Saldocontab
    template_name = 'finanzas/Slc_Panel.html'
    ordering = ['pk']
    paginate_by = 18


class Slc_Nuevo(CreateView):
        """Crear Saldocontab"""
        model = Saldocontab
        form_class = SaldocontabForm
        template_name = 'finanzas/Slc_New.html'
        success_url = reverse_lazy('finanzas:slc_panel')

        def form_invalid(self, form):
            messages.error(self.request, 'Hay un error en el formulario')
            return super(Slc_Nuevo, self).form_invalid(form)


class Slc_View(DetailView):
    """Visualiza Saldocontab"""
    template_name = 'finanzas/Slc_View.html'
    model = Saldocontab
    form_class = SaldocontabForm


class Slc_Edita(UpdateView):
    """Actualiza Saldocontabs"""
    model = Saldocontab
    form_class = SaldocontabForm
    template_name = 'finanzas/Slc_Edit.html'
    success_url = reverse_lazy('finanzas:slc_panel')


class Slc_Delet(DeleteView):
    """Elimina Saldocontabs"""
    model = Saldocontab
    form_class = SaldocontabForm
    template_name = 'finanzas/Slc_Delet.html'
    success_url = reverse_lazy('finanzas:slc_panel')

# ===================================================================================== #
# ------------------| C O M P R O B A N T E S     C O N T A B L E S |------------------ #
# ===================================================================================== #


class Cmp_Lista(ListView):
    """Listado de Comprobante"""
    model = Comprobante
    template_name = 'finanzas/Cmp_Panel.html'
    ordering = ['pk']
    paginate_by = 18


class Cmp_Nuevo(CreateView):
        """Crear Comprobante"""
        model = Comprobante
        form_class = ComprobanteForm
        template_name = 'finanzas/Cmp_New.html'
        success_url = reverse_lazy('finanzas:cmp_panel')

        def form_invalid(self, form):
            messages.error(self.request, 'Hay un error en el formulario')
            return super(Cmp_Nuevo, self).form_invalid(form)

# class Cpm_Buscar(TemplateView):


class Cmp_View(DetailView):
    """Visualiza Comprobante"""
    template_name = 'finanzas/Cmp_View.html'
    model = Comprobante
    form_class = ComprobanteForm


class Cmp_Edita(UpdateView):
    """Actualiza Comprobantes"""
    model = Comprobante
    form_class = ComprobanteForm
    template_name = 'finanzas/Cmp_Edit.html'
    success_url = reverse_lazy('finanzas:cmp_panel')


class Cmp_Delet(DeleteView):
    """Elimina Comprobantes"""
    model = Comprobante
    form_class = SaldocontabForm
    template_name = 'finanzas/Cmp_Delet.html'
    success_url = reverse_lazy('finanzas:cmp_panel')
# class Cpm_Print(ListView):
