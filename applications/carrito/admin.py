from django.contrib import admin
from .models import (
    Carrito,
    DetalleCarrito
)
# Register your models here.


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        
    ]
@admin.register(DetalleCarrito)
class DetalleCarritoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
    ]
    
