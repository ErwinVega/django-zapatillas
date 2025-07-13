from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import VariantProduct
from applications.venta.models import Pedido
from .utils import CacheManager


from typing import List
from django.core.cache import cache


@receiver(post_save, sender=VariantProduct)
def update_variant_price(sender, instance, created, **kwargs):
    if not created:
        
        # Limpiar la caché para el detalle del producto variante
        CacheManager.clear_variant_detail_cache(instance.id)
        # cache_key_detail = f"variant_detail_{instance.pk}"
        # cache.delete(cache_key_detail)
        
        # Limpiar la caché para la lista de variantes de producto
        CacheManager.clear_variant_list_cache()
        #cache.delete_pattern("product_variant_list_*",)
        
        
       # No tiene sentido actualizar el precio ya que ya esta hecho el pedido
        # print(f"Objecto actualizado {instance}")
        # pedidos_afectados:List[Pedido]  =  Pedido.objects.filter(detalles__producto=instance)
        
        # for pedido in pedidos_afectados:
        #     pedido.calculate_total()