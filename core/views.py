from django.shortcuts import render
from properties.models import Property


def home(request):
    destaques = Property.objects.filter(ativo=True).order_by("-criado_em")[:8]
    return render(request, "core/home.html", {"destaques": destaques})
