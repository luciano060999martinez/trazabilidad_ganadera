from django.contrib import admin
from . import models
from . import models

@admin.register(models.Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('codigo_animal', 'estado_animal', 'propietario')
    search_fields = ('id',)
    #list_editable = ('estado',)


@admin.register(models.Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('propietario_nombre', 'propietario_apellido', 'propietario_ci')
# Register your models here.
