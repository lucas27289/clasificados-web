from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import *


# Create your views here.

def index(request):
    categorias = get_list_or_404(Categoria.objects.all())
    banners = get_list_or_404(Assets.objects.all().filter(ubicacion="banner"))
    bannerCount = banners.count
    return render(request, 'anuncios/index.html', {'categorias': categorias, 'banners': banners, 'bannerCount': bannerCount})

def categoria(request, cat):
    id_categoria = get_object_or_404(Categoria.objects.filter(nombre=cat))
    subcategoria = Subcategoria.objects.filter(id_categoria=id_categoria)
    return render(request, 'anuncios/categoria.html', {'subcategoria': subcategoria})