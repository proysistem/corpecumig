
from django.conf.urls import url
from apps.visitantes.views import Evn_Lista, Msg_Nuevo
from .views import Sol_Nuevo
from corporacion.utils import login_required_view

urlpatterns = [
    url(r'^Sol_Nuevo/$',   login_required_view(Sol_Nuevo.as_view()), name='sol_new'),
    # url(r'^Asp_Nuevo/$',                Asp_Nuevo.as_view(), name='asp_new'),
    url(r'^Evn_Panel',     login_required_view(Evn_Lista.as_view()), name='evn_panel'),
    url(r'^Msg_Nuevo/$',   login_required_view(Msg_Nuevo.as_view()), name='msg_new'),

]
