from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'updated')  # Asegúrate de incluir 'description' aquí
    search_fields = ('title', 'description')  # Campos por los que se puede buscar
    list_display_links = ('title', 'description')  # Actualiza list_display_links

    # Campos editables en el formulario de edición
    fields = ('title', 'description', 'image')

    # Si prefieres organizar los campos en secciones en el formulario de edición
    # fieldsets = (
    #     (None, {'fields': ('title', 'description')}),
    #     ('Imagen', {'fields': ('image',)}),
    # )