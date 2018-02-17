from django.conf.urls import url

from apps.inicio.views import IndexView, proyecto, propuesta, nosotros, contacto


urlpatterns = [
    url(r'^$', IndexView, name='iniciar'),
    url(r'^IndProy$', proyecto.as_view(), name='proyecto'),
    url(r'^IndProp$', propuesta, name='propuesta'),
    url(r'^IndNoso$', nosotros, name='nosotros'),
    url(r'^IndCont$', contacto, name='contacto'),
]
