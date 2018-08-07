from django.conf.urls import url

from .views import (Cjr_Lista, Cjr_Nuevo, Cjr_View,  Cjr_Edita, Cjr_Delet,
                    Cja_Lista, Cja_Nuevo, Cja_View,  Cja_Edita, Cja_Delet,
                    Mcj_Lista, Mcj_Nuevo, Mcj_View,  Mcj_Edita, Mcj_Delet,
                    Plc_Lista, Plc_Nuevo, Plc_Edita, Plc_View, Plc_Delet, Plc_Query,
                    Slc_Lista, Slc_Nuevo, Slc_View, Slc_Edita, Slc_Delet,
                    Cmp_Lista, Cmp_Nuevo, Cmp_View,  Cmp_Edita, Cmp_Delet)
from corporacion.utils import login_required_view


urlpatterns = [
    # url(r'^CjrPanel',                  login_required_view(Cjr_Lista.as_view()), name='cjr_panel'),
    # url(r'^CjrNuevo/$',                login_required_view(Cjr_Nuevo.as_view()), name='cjr_new'),
    # url(r'^CjrView/(?P<pk>\d+)/$', login_required_view(Cjr_View.as_view()),  name='cjr_view'),
    # url(r'^CjrEdita/(?P<pk>\d+)/$',    login_required_view(Cjr_Edita.as_view()), name='cjr_edit'),
    # url(r'^CjrElimina/(?P<pk>\d+)/$',  login_required_view(Cjr_Delet.as_view()), name='cjr_delet'),

    # url(r'^CjaPanel',                  login_required_view(Cja_Lista.as_view()), name='cja_panel'),
    # url(r'^CjaNuevo/$',                login_required_view(Cja_Nuevo.as_view()), name='cja_new'),
    # url(r'^CjaView/(?P<pk>\d+)/$', login_required_view(Cja_View.as_view()),  name='cja_view'),
    # url(r'^CjaEdita/(?P<pk>\d+)/$',    login_required_view(Cja_Edita.as_view()), name='cja_edit'),
    # url(r'^CjaElimina/(?P<pk>\d+)/$',  login_required_view(Cja_Delet.as_view()), name='cja_delet'),

    # # url(r'^MjaSearch',                 login_required_view(Mja_Buscar.as_view()), name='mja_search'),
    # url(r'^McjPanel',                  login_required_view(Mcj_Lista.as_view()), name='mcj_panel'),
    # url(r'^McjNuevo/$',                login_required_view(Mcj_Nuevo.as_view()), name='mcj_new'),
    # url(r'^McjView/(?P<pk>\d+)/$', login_required_view(Mcj_View.as_view()),  name='mcj_view'),
    # url(r'^McjEdita/(?P<pk>\d+)/$',    login_required_view(Mcj_Edita.as_view()), name='mcj_edit'),
    # url(r'^McjElimina/(?P<pk>\d+)/$',  login_required_view(Mcj_Delet.as_view()), name='mcj_delet'),

    url(r'^PlcPanel',                  login_required_view(Plc_Lista.as_view()), name='plc_panel'),
    # # url(r'^PlcSearch',                 login_required_view(Plc_Buscar.as_view()), name='plc_search'),
    # # url(r'^PlcPrint',                  login_required_view(Plc_Print.as_view()), name='plc_print'),
    # # url(r'^PlcPdf',                    login_required_view(Plc_Pdf.as_view()),   name='plc_pdf'),
    url(r'^PlcNuevo/$',                login_required_view(Plc_Nuevo.as_view()), name='plc_new'),
    # url(r'^PlcEdita/(?P<pk>\d+)/$',    login_required_view(Plc_Edita.as_view()), name='plc_edit'),
    url(r'^Plc_Query/(?P<plc_ncuenta>\d+)/$', login_required_view(Plc_Query.as_view()), name='plc_query'),
    # url(r'^PlcView/(?P<pk>\d+)/$', login_required_view(Plc_View.as_view()),  name='Plc_view'),
    # url(r'^PlcElimina/(?P<pk>\d+)/$',  login_required_view(Plc_Delet.as_view()), name='Plc_delet'),

    url(r'^SlcPanel',                  login_required_view(Slc_Lista.as_view()), name='slc_panel'),
    # url(r'^SlcNuevo/$',                login_required_view(Slc_Nuevo.as_view()), name='slc_new'),
    # # url(r'^SlcRepor',                  login_required_view(Slc_Repor.as_view()), name='slc_repor'),
    # url(r'^SlcView/(?P<pk>\d+)/$', login_required_view(Slc_View.as_view()),  name='slc_view'),
    # url(r'^SlcEdita/(?P<pk>\d+)/$',    login_required_view(Slc_Edita.as_view()), name='slc_edit'),
    # url(r'^SlcElimina/(?P<pk>\d+)/$',  login_required_view(Slc_Delet.as_view()), name='slc_delet'),

    # # url(r'^CmpSearch',                 login_required_view(Cmp_Buscar.as_view()), name='Cmp_search'),
    url(r'^CmpPanel',                  login_required_view(Cmp_Lista.as_view()), name='cmp_panel'),
    # url(r'^CmpNuevo/$',                login_required_view(Cmp_Nuevo.as_view()), name='cmp_new'),
    # url(r'^CmpView/(?P<pk>\d+)/$', login_required_view(Cmp_View.as_view()),  name='cmp_view'),
    # url(r'^CmpEdita/(?P<pk>\d+)/$',    login_required_view(Cmp_Edita.as_view()), name='cmp_edit'),
    # url(r'^CmpElimina/(?P<pk>\d+)/$',  login_required_view(Cmp_Delet.as_view()), name='cmp_delet'),
    # # url(r'^CmpPrint/(?P<pk>\d+)/$',    login_required_view(Cmp_Print.as_view()), name='cmp_print'),

]
