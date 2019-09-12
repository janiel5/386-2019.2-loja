from django.contrib import admin
from .models import Compra

# Register your models here.
class CompraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'unidadeCompra', 'qtdPrevistoMes', 'preco',
                    'precoMaximo')

admin.site.register(Compra, CompraAdmin)