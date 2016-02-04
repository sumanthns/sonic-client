import json

from config import CONF
from pi_client import PiClient


class Manager(object):
    def __init__(self, amqp_client):
        self.pi_client = PiClient()
        self.amqp_client = amqp_client

    def write_signal(self, opts):
        led = opts["led"]
        value = opts["output"]
        self.pi_client.output(led, value)
        self.ack_server("update_pin",
                        led="GPIO{}".format(led),
                        # output=self.pi_client.input(led),
                        output=value,
                        device_uuid=CONF.uuid)

    def ack_server(self, method, **kwargs):
        message = {method: kwargs}
        json_msg = json.dumps(message)
        self.amqp_client.publish(CONF.app_queue, json_msg)
