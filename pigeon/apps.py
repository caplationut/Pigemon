from django.apps import AppConfig


class PigeonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pigeon'

    # noinspection PyUnresolvedReferences
    def ready(self):
        import pigeon.signals
