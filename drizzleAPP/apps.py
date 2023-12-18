from django.apps import AppConfig
from multiprocessing import Process
from .views import update_cache

class DrizzleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drizzleAPP'

    def ready(self):
        proc = Process(target=update_cache)
        proc.start()
        proc.join()
