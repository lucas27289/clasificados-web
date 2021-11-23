from django.contrib import admin
from .models import Anuncio, Categoria, Subcategoria, Pagos, Imagen, User, Assets

# Register your models here.

admin.site.register(Anuncio)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Pagos)
admin.site.register(Imagen)
admin.site.register(User)
admin.site.register(Assets)