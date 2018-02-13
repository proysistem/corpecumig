from django.conf.urls import url

from apps.inicio.views import IndexView, proyecto, nosotros


urlpatterns = [
    url(r'^$', IndexView, name='iniciar'),
    url(r'^IndProy$', proyecto, name='proyecto'),
    url(r'^IndNoso$', nosotros, name='nosotros'),
]
