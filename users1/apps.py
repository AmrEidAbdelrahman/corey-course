from django.apps import AppConfig



class Users1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users1'

    def ready(self):
        import users1.signals