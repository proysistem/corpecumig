from django.conf.urls import url

from .views import IndexView, proyecto, propuesta, nosotros, Cnt_Nuevo, Reg_Nuevo, Req_Nuevo


urlpatterns = [
    url(r'^$', IndexView, name='iniciar'),
    url(r'^IndProy$', proyecto.as_view(), name='proyecto'),
    url(r'^IndProp$', propuesta, name='propuesta'),
    url(r'^IndNoso$', nosotros, name='nosotros'),
    url(r'^IndCont$', Cnt_Nuevo.as_view(), name='contacto'),
    url(r'^IndRegs$', Reg_Nuevo.as_view(), name='registro'),
    url(r'^IndReqi$', Req_Nuevo.as_view(), name='requiere'),
]
