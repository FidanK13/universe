from django.apps import AppConfig


class UniverseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'universe_app'
    #name = 'ecom_app'
    def ready(self):
        import universe_app.signals
