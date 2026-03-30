from django.contrib import admin
from .models import PropertyType, Property, PropertyImage


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo_anuncio", "cidade", "valor", "ativo", "destaque", "criado_em")
    list_filter = ("tipo_anuncio", "ativo", "destaque", "tipo_imovel")
    search_fields = ("titulo", "endereco", "cidade")
    list_editable = ("ativo", "destaque")
    prepopulated_fields = {"slug": ("titulo",)}
    date_hierarchy = "criado_em"


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ("imovel", "ordem", "legenda")