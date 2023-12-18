from django.apps import AppConfig
from multiprocessing import Process
from .views import update_cache

class DrizzleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drizzleAPP'

<<<<<<< HEAD
    def ready(self):
        proc = Process(target=update_cache)
        proc.start()
        proc.join()
=======

>>>>>>> 80dc8a9af9a7fa3aa6db8b01a5fc9b1acdc69bfd
