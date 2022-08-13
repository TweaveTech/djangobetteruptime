from .helpers import sound_alive

class SendHeartBeatMixin:
    def send_heartbeat(heartbeat_id=None, run_in_debug=False):
        '''
        Send a heartbeat to the given heartbeat_id
        '''
        heartbeat_id = heartbeat_id or self.heartbeat_id
        sound_alive(heartbeat_id)
