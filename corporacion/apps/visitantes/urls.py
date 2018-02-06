
from django.conf.urls import url
from apps.visitantes.views import AspNuevo, EvnLista, MsgNuevo


urlpatterns = [
    url(r'^visitantes/AspNuevo/$',                AspNuevo.as_view(), name='asp_new'),
    url(r'^visitantes/EvnPanel',                  EvnLista.as_view(), name='evn_panel'),
    url(r'^visitantes/MsgNuevo/$',                MsgNuevo.as_view(), name='msg_new'),
]
