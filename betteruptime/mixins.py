from .helpers import sound_alive

class SendHeartBeatMixin:
    @staticmethod
    def send_heartbeat(heartbeat_id, run_in_debug=False):
        '''
        Send a heartbeat to the given heartbeat_id
        '''
        sound_alive(heartbeat_id)