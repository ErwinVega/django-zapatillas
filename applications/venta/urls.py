from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CreatePedidoApiList,
    PedidoDetail,
    PedioModelViewSet
)
router = DefaultRouter()
router.register(r"api/pedidos",PedioModelViewSet,basename="pedidos")


# urlpatterns = [
#     path(
#         "api/pedido/create",
#         CreatePedidoApiList.as_view(),
#         name="create-pedido"
#     ),
#     path(
#         "api/pedido/<pk>",
#         PedidoDetail.as_view(),
#         name="pedido-detail"
#     )
# ]

urlpatterns = router.urls

