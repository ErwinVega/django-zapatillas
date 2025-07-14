from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from .models import (
    DetallePedido,
    Pedido
)
from .serializers import (
    PedidoSerializer
)


class CreatePedidoApiList(generics.CreateAPIView):
    queryset=Pedido.objects.all()
    serializer_class= PedidoSerializer
    permission_classes = [IsAuthenticated]



