from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest
from.models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    #comprobar si el usuario esta accediendo al panel de administrador es del grupo personal para no editar campos
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('created', 'updated', 'key', 'name')
        else:
            return ('created', 'updated')
admin.site.register(Link, LinkAdmin)