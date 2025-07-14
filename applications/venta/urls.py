from django.urls import path

from .views import (
    CreatePedidoApiList
)


urlpatterns = [
    path(
        "api/pedido/create",
        CreatePedidoApiList.as_view(),
        name="create-pedido"
    )
]
