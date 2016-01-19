from pi_client import PiClient


class Manager(object):

    def __init__(self):
        self.pi_client = PiClient()

    def write_signal(self, opts):
        led = opts["led"]
        value = opts["output"]
        self.pi_client.output(led, value)