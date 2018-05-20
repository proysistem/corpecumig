from django.conf.urls import url

from .views import (IndexView, proyecto, propuesta, nosotros, Cnt_Nuevo,
                    Reg_Nuevo, Req_Nuevo, Acc_Panel, Asp_Panel, Cnt_Panel, Req_Panel)


urlpatterns = [
    url(r'^$', IndexView, name='iniciar'),
    url(r'^IndProy$', proyecto.as_view(), name='proyecto'),
    url(r'^IndProp$', propuesta, name='propuesta'),
    url(r'^IndNoso$', nosotros, name='nosotros'),
    url(r'^IndCont$', Cnt_Nuevo.as_view(), name='contacto'),
    url(r'^IndRegs$', Reg_Nuevo.as_view(), name='registro'),
    url(r'^IndReqi$', Req_Nuevo.as_view(), name='requiere'),
    url(r'^AccPanel$', Acc_Panel.as_view(), name='acc_panel'),
    url(r'^CntPanel$', Cnt_Panel.as_view(), name='cnt_panel'),
    url(r'^ReqPanel$', Req_Panel.as_view(), name='req_panel'),
    url(r'^AspPanel$', Asp_Panel.as_view(), name='asp_panel'),
]
