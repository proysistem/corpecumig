from django.conf.urls import url

# from apps.inicio.views import IndexView, home

from apps.inicio.views import home, proyecto


urlpatterns = [
    # url(r'^$', IndexView, name='iniciar'),
    url(r'^$', home, name='home'),
    url(r'^$', proyecto, name='proyecto'),
]
