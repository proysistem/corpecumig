
from django.conf.urls import url
from apps.visitantes.views import Asp_Nuevo, Evn_Lista, Msg_Nuevo
from .views import Sol_Nuevo


urlpatterns = [
    url(r'^Sol_Nuevo/$',                Sol_Nuevo.as_view(), name='sol_new'),
    url(r'^Asp_Nuevo/$',                Asp_Nuevo.as_view(), name='asp_new'),
    url(r'^Evn_Panel',                  Evn_Lista.as_view(), name='evn_panel'),
    url(r'^Msg_Nuevo/$',                Msg_Nuevo.as_view(), name='msg_new'),

]
