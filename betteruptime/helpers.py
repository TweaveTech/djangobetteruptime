from django.apps import apps
import requests


def create_heartbeat_url(heartbeat_id):
	heartbeat_host = apps.get_app_config('betteruptime').heartbeat_host
	heartbeat_url = heartbeat_host + heartbeat_id
	return heartbeat_url


def sound_alive(heartbeat_id):
	url = create_heartbeat_url(heartbeat_id)
	requests.get(url)