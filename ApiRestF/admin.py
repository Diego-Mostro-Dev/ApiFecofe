from django.contrib import admin
from .models import Productos

class ProductosAdmin(admin.ModelAdmin):
    # Mostrar los campos que deseas en la lista de productos
    list_display = ('nombre', 'descripcion', 'precio', 'stock', 'imagen')

    # Permitir búsqueda por nombre
    search_fields = ('nombre',)

    # Agregar filtros en la barra lateral
    list_filter = ('precio', 'stock')

    # Configurar la visualización de los campos en el formulario de edición
    fields = ('nombre', 'descripcion', 'precio', 'stock', 'imagen')

admin.site.register(Productos, ProductosAdmin)
