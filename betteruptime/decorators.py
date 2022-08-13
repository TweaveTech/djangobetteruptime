import requests
from .helpers import sound_alive


def send_heartbeat(heartbeat_id, run_in_debug=False):
    '''
    Send a heartbeat to the given better-uptime url if the function ran successfully.
    If however the function failed, it should send a heartbeat at all.
    When better-uptime doesnt receive it's heartbeats in time, some action will be triggered.
    '''
    def dec_f(f):
        def wrap_f(*args, **kwargs):
            f_res = f(*args, **kwargs)
            sound_alive(heartbeat_id)
            return f_res
        return wrap_f
    return dec_f


def send_heartbeat_from_self(run_in_debug=False):
    """
    Send a heaartbeat to the better-updatime url, but get the id from self.heartbeat_id
    """
    def dec_f(f):
        def wrap_f(self, *args, **kwargs):
            f_res = f(self, *args, **kwargs)
            sound_alive(self.heartbeat_id)
            return f_res
        return wrap_f
    return dec_f

