# from functools import wraps
# import requests
from .helpers import sound_alive


# def send_heartbeat(heartbeat_id=None, run_in_debug=False):
#     '''
#     Send a heartbeat to the given better-uptime url if the function ran successfully.
#     If however the function failed, it should send a heartbeat at all.
#     When better-uptime doesnt receive it's heartbeats in time, some action will be triggered.
#     '''
#     def dec_f(f):
#         @wraps(f)
#         def wrap_f(self, *args, **kwargs):
#             f_res = f(self, *args, **kwargs)

#             if not heartbeat_id:
#                 heartbeat_id = self.heartbeat_id
                
#             sound_alive(heartbeat_id)

#             return f_res
#         return wrap_f
#     return dec_f


from django.apps import apps
import requests


def send_heartbeat(heartbeat_id=None, run_in_debug=False):
    '''
    Send a heartbeat to the given better-uptime url if the function ran successfully.
    If however the function failed, it should send a heartbeat at all.
    When better-uptime doesnt receive it's heartbeats in time, some action will be triggered.
    '''
    def dec_f(f):
        def wrap_f(*args, **kwargs):
            f_res = f(*args, **kwargs)

            sound_alive(heartbeat_id)
            # heartbeat_host = apps.get_app_config('betteruptime').heartbeat_host
            # heartbeat_url = heartbeat_host + heartbeat_id
            # requests.get(heartbeat_url)
            return f_res
        return wrap_f
    return dec_f


