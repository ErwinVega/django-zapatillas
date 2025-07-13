from django.contrib import admin
from django.utils.html import format_html

# FIXME: MODELS
from .models import (
    Brand,
    VariantProduct,
    Product,
    ImagesProductVariant
)

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10
    ordering = ('id',)
    
class ImageInline(admin.TabularInline):
    model = ImagesProductVariant
    extra = 1
    
@admin.register(VariantProduct)
class VariantProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color',  'stock', 'price','size', 'image_preview')
    search_fields = ('product__name', 'color','size',"id")
    list_filter = ('product__brand', 'color', 'size')
    list_per_page = 10
    ordering = ('id',)
    inlines = [ImageInline]
    
    def image_preview(self, obj):
        if obj.images.exists():
            return format_html(
                '<a href="{url}" target="_blank">'
                '<img src="{url}" style="width: 50px; height: 50px; object-fit: cover;"/>'
                '</a>',
                url=obj.images.first().image if obj.images.exists() else '#'
            )
        return "No Image"
    image_preview.short_description = 'Image'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'description')
    search_fields = ('name', 'brand__name')
    list_filter = ('brand',)
    ordering = ('id',)
    list_per_page = 10
    
admin.site.register(ImagesProductVariant)    

