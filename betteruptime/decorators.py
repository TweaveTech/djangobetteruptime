from django.apps import apps
import requests


def send_heartbeat(heartbeat_id, run_in_debug=False):
    '''
    Send a heartbeat to the given better-uptime url if the function ran successfully.
    If however the function failed, it should send a heartbeat at all.
    When better-uptime doesnt receive it's heartbeats in time, some action will be triggered.
    '''
    def dec_f(f):
        def wrap_f(*args, **kwargs):
            f_res = f(*args, **kwargs)
            heartbeat_host = apps.get_app_config('betteruptime').heartbeat_host
            heartbeat_url = heartbeat_host + heartbeat_id
            requests.get(heartbeat_url)
            return f_res
        return wrap_f
    return dec_f
