from django.conf.urls import url
from .views import (Soc_Panel, Soc_Nuevo, Soc_View, Soc_Edita, Soc_Delet, Pop_Opcion,
                    Cso_Panel, Cso_Nuevo, Cso_View, Cso_Edita, Cso_Delet)
from corporacion.utils import login_required_view


urlpatterns = [
    url(r'^PopOpcion$', Pop_Opcion, name='pop_opcion'),
    url(r'^SocPanel',                  (Soc_Panel.as_view()), name='soc_panel'),
    url(r'^SocNuevo/$',                (Soc_Nuevo.as_view()), name='soc_new'),
    url(r'^SocView/$',     login_required_view(Soc_View.as_view()),  name='soc_view'),
    url(r'^SocEdita/$',    login_required_view(Soc_Edita.as_view()), name='soc_edit'),
    url(r'^SocElimina/(?P<pk>\d+)/$',  login_required_view(Soc_Delet.as_view()), name='soc_delet'),

    url(r'^CsoPanel',                  (Cso_Panel.as_view()), name='cso_panel'),
    url(r'^CsoNuevo/$',                (Cso_Nuevo.as_view()), name='cso_new'),
    url(r'^CsoView/$',     login_required_view(Cso_View.as_view()),  name='cso_view'),
    url(r'^CsoEdita/$',    login_required_view(Cso_Edita.as_view()), name='cso_edit'),
    url(r'^CsoElimina/(?P<pk>\d+)/$',  login_required_view(Cso_Delet.as_view()), name='cso_delet'),
]
