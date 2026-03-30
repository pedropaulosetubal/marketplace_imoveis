from django.shortcuts import render
from properties.models import Property

def home(request):
    destaques = Property.objects.filter(destaque=True, ativo=True)[:6]
    return render(request, 'core/home.html', {'destaques': destaques})