import uuid
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from applications.producto.models import VariantProduct


class Pedido(models.Model):
    id= models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.user} - Total: {self.total}"
    
    def calculate_total(self):
        self.total = sum(detalle.producto.price * detalle.cantidad for detalle in self.detalles.all())
        self.save(update_fields=['total'])
        return self.total


class DetallePedido(models.Model):
    id= models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(VariantProduct, on_delete=models.CASCADE, related_name='detalles')
    cantidad = models.PositiveIntegerField()
    
    
    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=["pedido","producto"],
                name="unique_pedido_producto"
            )
        ]

    def __str__(self):
        return f"Detalle {self.id} - Pedido: {self.pedido.id} - Producto: {self.producto} - Cantidad: {self.cantidad}"
    
    
    def save(self,*args, **kwargs):
        
        self.pedido.calculate_total()
        super().save(*args, **kwargs)
        
    def delete(self,*args, **kwargs):
        self.pedido.calculate_total()
        super().delete(*args, **kwargs)
        
    