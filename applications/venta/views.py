from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet

from rest_framework import generics

from .models import (
    Pedido
)
from .serializers import (
    PedidoSerializer
)

class PedioModelViewSet(ModelViewSet):
    queryset=Pedido.objects.all()
    serializer_class= PedidoSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        queryset= Pedido.objects.filter(user=self.request.user)
        return queryset
    
    


