from django.contrib import admin

from .models import Individuo, Fuente, Evento, Documento, Ubicacion


admin.site.register(Individuo)
admin.site.register(Evento)
admin.site.register(Fuente)
admin.site.register(Documento)
admin.site.register(Ubicacion)