from django.apps import AppConfig


class BetteruptimeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'betteruptime'
    heartbeat_host = "https://uptime.betterstack.com/api/v1/heartbeat/"
