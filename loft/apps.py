from django.apps import AppConfig


class LoftConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loft'

    def ready(self):
        pass
