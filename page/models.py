from django.db import models
from django.utils import timezone
from django.contrib import admin


class Cancion(models.Model):
    Titulo = models.CharField(max_length=200)
    Anio = models.CharField(max_length=200)
    Duracion =models.CharField(max_length=200)
    Generos = (
	    ('Salsa', 'Salsa'),
	    ('Bachata', 'Bachata'),
	    ('Rock', 'Rock'),
	    ('Merenge', 'Merenge'),
	    ('Cumbia', 'Cumbia'),
	    )
    Genero = models.CharField(
	    max_length=10,
	    choices=Generos,
	    default='Salsa',
	    )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Titulo

class Artista(models.Model):
    Nombre_artista = models.CharField(max_length=130)
    Lugar_nacimiento = models.CharField(max_length=130)
    Fecha_Nacimiento = models.DateField()
    def __str__(self):
        return self.Nombre_artista

class Colaboracion(models.Model):
    Cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    Artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

class ColaboracionInLine(admin.TabularInline):
    model = Colaboracion
    extra = 1


class CancionAdmin(admin.ModelAdmin):
    inlines = (ColaboracionInLine,)


class ArtistaAdmin (admin.ModelAdmin):
    inlines = (ColaboracionInLine,)