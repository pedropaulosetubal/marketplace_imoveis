from django import forms
from .models import Property, PropertyType


class PropertySearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="Buscar",
        widget=forms.TextInput(attrs={"placeholder": "Cidade, bairro, título..."}),
    )
    tipo_anuncio = forms.ChoiceField(
        required=False,
        label="Tipo",
        choices=[("", "Todos")] + list(Property.TIPO_ANUNCIO),
    )
    tipo_imovel = forms.ModelChoiceField(
        PropertyType.objects.all(),
        required=False,
        label="Categoria",
        empty_label="Todos",
    )
    valor_min = forms.DecimalField(
        required=False,
        label="Valor mín.",
        min_value=0,
        widget=forms.NumberInput(attrs={"placeholder": "0"}),
    )
    valor_max = forms.DecimalField(
        required=False,
        label="Valor máx.",
        min_value=0,
        widget=forms.NumberInput(attrs={"placeholder": "Qualquer"}),
    )
    quartos = forms.IntegerField(
        required=False,
        min_value=0,
        label="Mín. quartos",
        widget=forms.NumberInput(attrs={"placeholder": "0"}),
    )
