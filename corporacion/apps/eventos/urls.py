
from django.conf.urls import url
from django.contrib import admin
from apps.eventos.views import (AspLista, AspNuevo, AspView, AspEdita, AspDelet, EvnLista, EvnNuevo, EvnView, EvnEdita,
                                EvnDelet, MsgLista, MsgNuevo, MsgView, MsgEdita, MsgDelet, ZipLista, ZipNuevo, ZipView,
                                ZipEdita, ZipDelet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^AspPanel',                  AspLista.as_view(), name='asp_panel'),
    url(r'^AspNuevo/$',                AspNuevo.as_view(), name='asp_new'),
    url(r'^AspConsulta/(?P<pk>\d+)/$', AspView.as_view(),  name='asp_view'),
    url(r'^AspEdita/(?P<pk>\d+)/$',    AspEdita.as_view(), name='asp_edit'),
    url(r'^AspElimina/(?P<pk>\d+)/$',  AspDelet.as_view(), name='asp_delet'),

    url(r'^EvnPanel',                  EvnLista.as_view(), name='evn_panel'),
    url(r'^EvnNuevo/$',                EvnNuevo.as_view(), name='evn_new'),
    url(r'^EvnConsulta/(?P<pk>\d+)/$', EvnView.as_view(),  name='evn_view'),
    url(r'^EvnEdita/(?P<pk>\d+)/$',    EvnEdita.as_view(), name='evn_edit'),
    url(r'^EvnElimina/(?P<pk>\d+)/$',  EvnDelet.as_view(), name='evn_delet'),

    url(r'^MsgPanel',                  MsgLista.as_view(), name='msg_panel'),
    url(r'^MsgNuevo/$',                MsgNuevo.as_view(), name='msg_new'),
    url(r'^MsgConsulta/(?P<pk>\d+)/$', MsgView.as_view(),  name='msg_view'),
    url(r'^MsgEdita/(?P<pk>\d+)/$',    MsgEdita.as_view(), name='msg_edit'),
    url(r'^MsgElimina/(?P<pk>\d+)/$',  MsgDelet.as_view(), name='msg_delet'),

    url(r'^ZipPanel',                  ZipLista.as_view(), name='zip_panel'),
    url(r'^ZipNuevo/$',                ZipNuevo.as_view(), name='zip_new'),
    url(r'^ZipConsulta/(?P<pk>\d+)/$', ZipView.as_view(),  name='zip_view'),
    url(r'^ZipEdita/(?P<pk>\d+)/$',    ZipEdita.as_view(), name='zip_edit'),
    url(r'^ZipElimina/(?P<pk>\d+)/$',  ZipDelet.as_view(), name='zip_delet'),

]
