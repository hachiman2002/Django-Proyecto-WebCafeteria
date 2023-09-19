from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #mostrar columnas
    list_display = ('title', 'author', 'published', 'post_categories')
    #ordenar campos
    ordering = ('author',)
    #formulario de busqueda
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    #filtrar por fechas
    date_hierarchy = 'published'
    #filtrar por 
    list_filter = ('author__username', 'categories__name')
    
    #funcion para filtrar por categorias
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    #se muestra el nombre de la funcion, debemos cambiarlo
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)