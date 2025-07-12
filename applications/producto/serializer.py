from rest_framework import serializers,pagination
from .models import (
    Brand,
    VariantProduct,
    ImagesProductVariant
)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
        
class VariantImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesProductVariant
        fields = ['image']
class VariantProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='product.brand.name', read_only=True)
    category = serializers.CharField(source='product.category.name', read_only=True)
    images = VariantImagesSerializer(many=True, read_only=True)
    class Meta:
        model = VariantProduct
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = instance.product.name if instance.product else None
        return representation
    
    

class VariantProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='product.brand.name', read_only=True)
    images = VariantImagesSerializer(many=True, read_only=True)
    description = serializers.CharField(source='product.description', read_only=True)
    
    class Meta:
        model = VariantProduct
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = instance.product.name if instance.product else None
        return representation  
    
class PaginatorSerializer(pagination.PageNumberPagination):
    page_size = 10
    
    max_page_size = 100

    # def get_paginated_response(self, data):
    #     return {
    #         'count': self.page.paginator.count,
    #         'next': self.get_next_link(),
    #         'previous': self.get_previous_link(),
    #         'results': data
    #     }