from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "estado", "tiene_imagen", "fecha_creacion")
    list_filter = ("estado", "fecha_creacion")
    search_fields = ("titulo", "contenido", "autor")
    ordering = ("-fecha_creacion",)

    @admin.display(boolean=True, description="Imagen")
    def tiene_imagen(self, obj):
        return bool(obj.imagen)
