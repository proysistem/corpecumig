from django.contrib import admin
from apps.eventos.models import Zipcodigo, Evento, Mensaje


admin.site.register(Zipcodigo)
admin.site.register(Evento)
admin.site.register(Mensaje)
