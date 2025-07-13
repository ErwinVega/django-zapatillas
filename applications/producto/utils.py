from django.core.cache import cache

class CacheManager:
    @staticmethod
    def clear_variant_detail_cache(variant_id:str):
        cache_key_detail = f"variant_detail_{variant_id}"
        cache.delete(cache_key_detail)

    @staticmethod
    def clear_variant_list_cache():
        cache.delete_pattern("product_variant_list_*")
        