# views.py
import json
import os
import time
from django.http import JsonResponse
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status


from django_filters import rest_framework as filters


from .serializer import (
    BrandSerializer,
    VariantProductDetailSerializer,
    VariantProductSerializer,
    PaginatorSerializer
    )
from .models import (
    Brand,
    VariantProduct,
    Product,
    ImagesProductVariant
)

from .filter import (
    ProductVariantFilter
)

from django.conf import settings

class UploadMarcasView(APIView):

    def get(self, request, *args, **kwargs):
        # Ruta al archivo JSON interno (ajusta la ruta según donde lo tengas)
        productos_json = os.path.join(settings.BASE_DIR, 'applications/producto/productos.json')
        
        try:
            with open(productos_json, 'r') as file:
                data = json.load(file)
                
                # Insertar las marcas en la base de datos
                for item in data:
                    brand_name = item.get('brand')
                    if brand_name:
                        brand, created = Brand.objects.get_or_create(name=brand_name)
                        if created:
                            print(f"Marca '{brand_name}' creada.")
                        else:
                            print(f"Marca '{brand_name}' ya existe.")
                
                return JsonResponse({"message": "Proceso de carga de marcas completado."}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

   
class MarciasListView(generics.ListAPIView):
    queryset = Brand.objects.filter(image__isnull=False).order_by("id")
    serializer_class = BrandSerializer
    
class ProductVariantListView(generics.ListAPIView):
    
    queryset = VariantProduct.objects.all().order_by("id")

    serializer_class = VariantProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductVariantFilter
    pagination_class=PaginatorSerializer
    
    
    
    def list(self, request, *args, **kwargs):
        response =super().list(request, *args, **kwargs)
        query_params=request.query_params.dict()
        cache_key = f"product_variant_list_{hash(frozenset(query_params.items()))}"
        
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
       
        print("traido desde postgresql")
        cache.set(cache_key, response.data, timeout=60*30)  # Cache for 2 minutes
        return response
        
    
    
class DetailVariantProductiView(generics.RetrieveAPIView):
    queryset = VariantProduct.objects.all()
    serializer_class = VariantProductDetailSerializer
    throttle_classes= []
    
    def retrieve(self, request, *args, **kwargs):
        cache_key = f"variant_detail_{kwargs['pk']}"
        cached_data = cache.get(cache_key)
        if cached_data:
            print("traido desde cache")
            return Response(cached_data)
        response =super().retrieve(request, *args, **kwargs)
        cache.set(cache_key,response.data, timeout=60*30)  # Cache for 2 minutes
        print("traido desde postgresql")
        return response
    
    



class CreateJsonProductVariant(APIView):
    def get(self, request, *args, **kwargs):
        # Ruta al archivo JSON interno (ajusta la ruta según donde lo tengas)
        productos_json = os.path.join(settings.BASE_DIR, 'applications/producto/data_limpia.json')
        
        try:
            with open(productos_json, 'r',encoding="utf-8") as file:
                data = json.load(file)
                
                # Insertar los productos en la base de datos
                for item in data:
                    brand_name = item.get('brand')
                    product_name = item.get('name')
                    description = item.get('description', '')
                    if brand_name:
                        brand, created = Brand.objects.get_or_create(name=brand_name)
                    if product_name:
                        product, created = Product.objects.get_or_create(name=product_name, brand=brand, description=description)
                    product_variant , created = VariantProduct.objects.get_or_create(
                        product=product,
                        color=item.get('color', ''),
                        size=item.get('size', 38),  # Asignar un valor por defecto si no está presente
                        stock=item.get('stock', 1),  # Asignar un valor por defecto si no está presente
                        price=item.get('price', 0.0),  # Asignar un valor por defecto si no está presente
                        is_top_seller=item.get('is_top_seller', False),
                        is_new=item.get('is_new', True),
                    )
                    for image_url in item.get('imagenes', []):
                        # Aquí podrías agregar lógica para manejar las imágenes si es necesario
                        # Por ejemplo, podrías crear un modelo de imagen relacionado con VariantProduct
                        ImagesProductVariant.objects.get_or_create(product=product_variant, image=image_url)

                # Aquí podrías agregar lógica para insertar productos y variantes si es necesario
                # Empezar a insertar productos y variantes
                
                
                return JsonResponse({"message": "Proceso de carga de marcas completado."}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)