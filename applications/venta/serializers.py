from rest_framework import serializers



from .models import (
    Pedido,
    DetallePedido
)

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = "__all__"
        read_only_fields = (
            "id",
            "pedido",
        )

class PedidoSerializer(serializers.ModelSerializer):
    detalles= DetallePedidoSerializer(many=True)
    class Meta:
        model = Pedido
        fields = "__all__"
        read_only_fields = (
            "id",
            "user",
            "total",
        )
        
    def create(self, validated_data):
        user = self.context["request"].user
        detalles= validated_data.pop("detalles")
        
        pedido = Pedido.objects.create(user=user,**validated_data)
        print(detalles)
        
        for detalle in detalles:
            DetallePedido.objects.create(pedido=pedido,**detalle)
        
        
        return pedido
        
    