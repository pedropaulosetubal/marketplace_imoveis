from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Property
from .forms import PropertySearchForm


def list_view(request):
    form = PropertySearchForm(request.GET or None)
    qs = Property.objects.filter(ativo=True).select_related("tipo_imovel")

    if form.is_valid():
        data = form.cleaned_data
        if data.get("q"):
            qs = qs.filter(
                Q(titulo__icontains=data["q"])
                | Q(descricao__icontains=data["q"])
                | Q(cidade__icontains=data["q"])
                | Q(endereco__icontains=data["q"])
            )
        if data.get("tipo_anuncio"):
            qs = qs.filter(tipo_anuncio=data["tipo_anuncio"])
        if data.get("tipo_imovel"):
            qs = qs.filter(tipo_imovel=data["tipo_imovel"])
        if data.get("valor_min") is not None:
            qs = qs.filter(valor__gte=data["valor_min"])
        if data.get("valor_max") is not None:
            qs = qs.filter(valor__lte=data["valor_max"])
        if data.get("quartos") is not None and data["quartos"] > 0:
            qs = qs.filter(quartos__gte=data["quartos"])

    paginator = Paginator(qs, 12)
    page = request.GET.get("page", 1)
    page_obj = paginator.get_page(page)

    return render(
        request,
        "properties/list.html",
        {"form": form, "page_obj": page_obj},
    )


def detail_view(request, slug):
    imovel = get_object_or_404(Property, slug=slug, ativo=True)
    return render(request, "properties/detail.html", {"imovel": imovel})
