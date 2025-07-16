from rest_framework import serializers
from .models import (
    Carrito,
    DetalleCarrito
)


class DetalleCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model= DetalleCarrito
        fields = "__all__"
        fields_read_only= ("user","id")
        
    def create(self, validated_data):
        user=self.context["request"].user
        validated_data.pop("user")
        validated_data["user"]= user
        return validated_data
    
        
        
        
class CarritoSerializer(serializers.ModelSerializer):
    detalle_carrito= DetalleCarritoSerializer(many=True)
    class Meta:
        model = Carrito
        fields = "__all__"
        fields_read_only= (
            "id",
            "created"
        )
    
    
    def create(self, validated_data):
        user= self.context["request"].user
        detalle_carrito= validated_data.pop("detalle_carrito")
        carrito,created = Carrito.objects.get_or_create(user=user)
        
        for detalle in detalle_carrito:
            DetalleCarrito.objects.create(carrito=carrito,**detalle)
        
        return super().create(validated_data)
    



