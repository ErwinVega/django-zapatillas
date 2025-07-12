from django_filters import rest_framework as filters


from .models  import (
    VariantProduct
)


class ProductVariantFilter(filters.FilterSet):
    product_name = filters.CharFilter(field_name="product__name", lookup_expr="icontains")
    brand = filters.CharFilter(field_name="product__brand__name",lookup_expr="iexact")
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    is_top_seller = filters.BooleanFilter(field_name="is_top_seller")
    is_new = filters.BooleanFilter(field_name="is_new")

   