from django.contrib import admin
from .models import Producto, Categoria, Usuario, Rol, Imagen

class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 1  

class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenInline]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Imagen)
