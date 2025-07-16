from rest_framework.routers import DefaultRouter


from .views import (
    ModelViewSetDetalleCarrito
)

router = DefaultRouter()

router.register(r"api/carrito",ModelViewSetDetalleCarrito,basename="carrito")


urlpatterns = router.urls
