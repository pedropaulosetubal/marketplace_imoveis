from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import PropertyType, Property, PropertyImage

# Tamanho máximo de upload (5 MB)
MAX_IMAGE_SIZE_MB = 5
MAX_IMAGE_BYTES = MAX_IMAGE_SIZE_MB * 1024 * 1024


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = "__all__"  

    def clean_imagem(self):
        arquivo = self.cleaned_data.get("imagem")
        if arquivo and hasattr(arquivo, "size") and arquivo.size > MAX_IMAGE_BYTES:
            raise ValidationError(f"Imagem não pode ter mais de {MAX_IMAGE_SIZE_MB} MB.")
        return arquivo


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    form = PropertyImageForm
    extra = 1


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
    inlines = [PropertyImageInline]
    date_hierarchy = "criado_em"


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ("imovel", "ordem", "legenda")
