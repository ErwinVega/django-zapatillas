from django.contrib import admin

# Register your models here.
from .models import Pedido, DetallePedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'created','updated')
    search_fields = ('user__username',)
    list_filter = ('created',)
    
    
@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'producto', 'cantidad')
    search_fields = ('pedido__id', 'producto__name')
    list_filter = ('pedido__created',)    