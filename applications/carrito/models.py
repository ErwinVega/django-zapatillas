
from decimal import Decimal
from django.db import models
import uuid
# Create your models here.

from django.contrib.auth.models import User
from applications.producto.models import VariantProduct


class Carrito(models.Model):
    id= models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrito')

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.user}"



class DetalleCarrito(models.Model):
    id= models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='detalles_carrito')
    producto:VariantProduct = models.ForeignKey(VariantProduct, on_delete=models.CASCADE, related_name='detalles_carrito')
    cantidad = models.PositiveIntegerField()
    
    
    class Meta:
        unique_together = ['carrito', 'producto']
        
    @property
    def sub_total(self)->Decimal:
        return self.producto.price * self.cantidad

    def __str__(self):
        return f"Detalle {self.id} - Pedido: {self.carrito.id} - Producto: {self.producto} - Cantidad: {self.cantidad}"
    

        
    