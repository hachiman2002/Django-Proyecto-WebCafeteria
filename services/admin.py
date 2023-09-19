from django.contrib import admin
from .models import Service

# Register your models here.

#Mostrar fecha y actualizacion de un proyecto
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

#resgistrando en la pagina de administrador
admin.site.register(Service, ServiceAdmin)