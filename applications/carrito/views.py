from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import (
    Carrito,
    DetalleCarrito
)
from .serializers import (
    DetalleCarritoSerializer
)
from rest_framework.viewsets import ModelViewSet

class ModelViewSetDetalleCarrito(ModelViewSet):
    serializer_class=[DetalleCarritoSerializer]
    
    def get_queryset(self):
        user= self.request.user
        queryset = DetalleCarrito.objects.filter(user)
        return queryset


