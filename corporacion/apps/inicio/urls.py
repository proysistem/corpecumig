from django.conf.urls import url

from apps.inicio.views import IndexView, proyecto


urlpatterns = [
    url(r'^$', IndexView, name='iniciar'),
    url(r'^IndProy$', proyecto, name='proyecto'),
]
