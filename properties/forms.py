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

    CIDADES_DF = [
        ("Plano Piloto", "Plano Piloto"),
        ("Gama", "Gama"),
        ("Taguatinga", "Taguatinga"),
        ("Brazlândia", "Brazlândia"),
        ("Sobradinho", "Sobradinho"),
        ("Planaltina", "Planaltina"),
        ("Paranoá", "Paranoá"),
        ("Núcleo Bandeirante", "Núcleo Bandeirante"),
        ("Ceilândia", "Ceilândia"),
        ("Guará", "Guará"),
        ("Cruzeiro", "Cruzeiro"),
        ("Samambaia", "Samambaia"),
        ("Santa Maria", "Santa Maria"),
        ("São Sebastião", "São Sebastião"),
        ("Recanto das Emas", "Recanto das Emas"),
        ("Lago Sul", "Lago Sul"),
        ("Riacho Fundo", "Riacho Fundo"),
        ("Lago Norte", "Lago Norte"),
        ("Candangolândia", "Candangolândia"),
        ("Águas Claras", "Águas Claras"),
        ("Riacho Fundo II", "Riacho Fundo II"),
        ("Sudoeste/Octogonal", "Sudoeste/Octogonal"),
        ("Varjão", "Varjão"),
        ("Park Way", "Park Way"),
        ("SCIA / Estrutural", "SCIA / Estrutural"),
        ("Sobradinho II", "Sobradinho II"),
        ("Jardim Botânico", "Jardim Botânico"),
        ("Itapoã", "Itapoã"),
        ("SIA", "SIA"),
        ("Vicente Pires", "Vicente Pires"),
        ("Fercal", "Fercal"),
        ("Sol Nascente / Pôr do Sol", "Sol Nascente / Pôr do Sol"),
        ("Arniqueira", "Arniqueira"),
    ]

    cidade = forms.ChoiceField(
        required=False,
        label="Cidade",
        choices=[("", "Todas as cidades")] + CIDADES_DF,
    )
