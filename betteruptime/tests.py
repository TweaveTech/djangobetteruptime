from unittest.mock import patch, MagicMock
from django.test import SimpleTestCase
from django.conf import settings

settings.configure(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})
class HeartBeatTests(SimpleTestCase):
    def setUp(self):
        super().setUp()
        self.heartbeat_id = 'MjSDWT5u6dBmTiJGdHJ5FW5x'
        self.heartbeat_host = "https://uptime.betterstack.com/api/v1/heartbeat/"
        self.expected_url = self.heartbeat_host + self.heartbeat_id

    def create_heartbeat_url(self):
        return self.heartbeat_host + self.heartbeat_id

    @patch('betteruptime.helpers.create_heartbeat_url', new=lambda heartbeat_id: "https://uptime.betterstack.com/api/v1/heartbeat/" + heartbeat_id)
    def test_sound_alive(self):
        from .helpers import sound_alive

        response = sound_alive(self.heartbeat_id)

        # Check the status code
        self.assertEqual(response.status_code, 200)

        # Check the URL used
        self.assertEqual(response.url, self.expected_url)

    @patch('betteruptime.helpers.create_heartbeat_url', new=lambda heartbeat_id: "https://uptime.betterstack.com/api/v1/heartbeat/" + heartbeat_id)
    @patch('betteruptime.helpers.sound_alive')
    def test_send_heartbeat_decorator(self, mock_sound_alive):
        from .decorators import send_heartbeat

        @send_heartbeat(heartbeat_id=self.heartbeat_id)
        def test_function():
            return True

        result = test_function()
        self.assertTrue(result)
        mock_sound_alive.assert_called_once_with(self.heartbeat_id)
