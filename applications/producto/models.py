from django.db import models
from .choices import SisesChoices


# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image= models.URLField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        
class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='products')
    description = models.TextField()   
    def __str__(self):
        return f"{self.brand.name} - {self.name}"
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class VariantProduct(models.Model):
    

    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='variants')
    color = models.CharField(max_length=50)
    size = models.PositiveIntegerField(choices=SisesChoices.choices, default=38)    
    stock = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_top_seller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.id}"
    
    class Meta:
        verbose_name = 'Variante Producto'
        verbose_name_plural = 'Variantes Productos'
        

        
        
        
class ImagesProductVariant(models.Model):
    product = models.ForeignKey(VariantProduct, on_delete=models.CASCADE,related_name='images')
    image = models.URLField(max_length=250)

    def __str__(self):
        return f"Imagen de {self.product.product.name}"
    
    class Meta:
        verbose_name = 'Imagen Producto'
        verbose_name_plural = 'Imagenes Productos'
        
        
