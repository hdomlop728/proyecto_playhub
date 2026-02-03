from django.contrib import admin
from .models import Juego

# Register your models here.

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'precio', 'fecha_lanzamiento')
    search_fields = ('titulo',)
    list_filter = ('plataforma',)


    fieldsets = [
         ('Informacion', {
             'fields': [
                 'titulo',
                 'plataforma',
             ],
         }),
         ('Detalles', {
             'fields': [
                 'precio',
                 'fecha_lanzamiento',
             ]
         }
         )
     ]