from django.apps import AppConfig


class ProductoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.producto'
    def ready(self):
        import applications.producto.signals
        # Ensure signals are imported and connected
