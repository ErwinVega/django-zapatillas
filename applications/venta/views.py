from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet

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
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class PedidoDetail(generics.RetrieveAPIView):
    queryset=Pedido.objects.all()
    serializer_class= PedidoSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
class PedioModelViewSet(ModelViewSet):
    queryset=Pedido.objects.all()
    serializer_class= PedidoSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        queryset= Pedido.objects.filter(user=self.request.user)
        return queryset


