from django.conf.urls import url

from .views import IndexView, proyecto, propuesta, nosotros, Cnt_Nuevo


urlpatterns = [
    url(r'^$', IndexView, name='iniciar'),
    url(r'^IndProy$', proyecto.as_view(), name='proyecto'),
    url(r'^IndProp$', propuesta, name='propuesta'),
    url(r'^IndNoso$', nosotros, name='nosotros'),
    url(r'^IndCont$', Cnt_Nuevo.as_view(), name='contacto'),
]
