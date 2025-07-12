from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import VariantProduct
from applications.venta.models import Pedido


from typing import List


@receiver(post_save, sender=VariantProduct)
def update_variant_price(sender, instance, created, **kwargs):
    if not created:
       
        print(f"Objecto actualizado {instance}")
        pedidos_afectados:List[Pedido]  =  Pedido.objects.filter(detalles__producto=instance)
        
        for pedido in pedidos_afectados:
            pedido.calculate_total()