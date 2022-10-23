from django.apps import AppConfig


class EmailReplayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_replay'

    def ready(self):
        # Import celery app now that Django is mostly ready.
        # This initializes Celery and autodiscovers tasks
        import config.celery
