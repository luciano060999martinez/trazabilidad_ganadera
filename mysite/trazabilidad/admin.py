from django.contrib import admin
from . import models

@admin.register(models.Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    pass
# Register your models here.

@admin.register(models.Estado)
class EstadoAdmin(admin.ModelAdmin):
    pass