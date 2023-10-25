from django.contrib import admin

from .models import Contato,Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descriacao', 'preco')

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    
    
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Produto, ProdutoAdmin)