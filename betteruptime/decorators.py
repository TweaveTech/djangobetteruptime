from django.apps import apps
from .helpers import sound_alive
from .exceptions import NoHeartBeatIdError
import requests


def send_heartbeat(heartbeat_id=None, pass_if_none=True, run_in_debug=False):
    '''
    Send a heartbeat to the given better-uptime url if the function ran successfully.
    If however the function failed, it should send a heartbeat at all.
    When better-uptime doesnt receive it's heartbeats in time, some action will be triggered.
    '''
    def dec_f(f):
        def wrap_f(*args, **kwargs):
            f_res = f(*args, **kwargs)

            if heartbeat_id:
                sound_alive(heartbeat_id)
            else:
                try:
                    if args[0].heartbeat_id:
                        sound_alive(args[0].heartbeat_id)
                    else:
                        if not pass_if_none:
                            raise NoHeartBeatIdError()
                except AttributeError:
                    if not pass_if_none:
                        raise NoHeartBeatIdError()
            return f_res
        return wrap_f
    return dec_f


