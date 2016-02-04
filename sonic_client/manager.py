import json

from pi_client import PiClient
from sonic_client.amqp_client import publish_message
from sonic_client.config import CONF


class Manager(object):
    def __init__(self):
        self.pi_client = PiClient()

    def write_signal(self, opts):
        led = opts["led"]
        value = opts["output"]
        self.pi_client.output(led, value)
        self.ack_server("update_pin",
                        led=led,
                        output=self.pi_client.input(led),
                        device_uuid=CONF.uuid)

    def ack_server(self, method, **kwargs):
        message = {method: kwargs}
        json_msg = json.dumps(message)
        publish_message(CONF.app_queue, json_msg)
