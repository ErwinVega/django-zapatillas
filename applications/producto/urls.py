from django.urls import path

from .views import (
    UploadMarcasView,
    MarciasListView,
    ProductVariantListView,
    DetailVariantProductiView,
    CreateJsonProductVariant
    
)

urlpatterns = [
    path("/kk", UploadMarcasView.as_view(), name="upload_marcas"
    ),
    path(
        "api/marcas/list/",
        MarciasListView.as_view(),
        name="marcas_list",
    ),
    path(
        "api/variant/list/",
        ProductVariantListView.as_view(),
        name="variant_list",
        
    ),
    path(
        "api/variant/<int:pk>",
        DetailVariantProductiView.as_view(),
        name="variant-detail"
    ),
    path(
        "api/variant/create-json/",
        CreateJsonProductVariant.as_view(),
    ),
    path(
        "api/variant/<int:pk>/",
        DetailVariantProductiView.as_view(),
    )
]
