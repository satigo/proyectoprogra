from django.contrib import admin
from .models import Cancion,Artista,CancionAdmin,ArtistaAdmin

admin.site.register(Cancion, CancionAdmin)
admin.site.register(Artista, ArtistaAdmin)