import json
import pika
from sonic_client.config import CONF
from sonic_client.encryption import decrypt
from sonic_client.manager import Manager

QUEUE = CONF.get("client", "key")


class ActionUnsupportedError(Exception):
    def __init__(self, action):
        super(Exception, self).__init__("{} action is not"
                                        "supported by sonic"
                                        "client".format(action))


class SonicClient(object):
    def __init__(self, logger):
        self.amqp_channel = _create_amqp_channel()
        self.amqp_channel.queue_declare(queue=QUEUE)
        self.manager = Manager()
        self.logger = logger

    def _callback(self, ch, method, properties, body):
        self.logger.debug("Processing {}".format(body))
        try:
            message = json.loads(decrypt(body))
            for key, val in message.iter_items():
                if hasattr(self.manager, key):
                    getattr(self.manager, key)(val)
                else:
                    raise ActionUnsupportedError(key)
        except Exception as e:
            self.logger.error("Error while processing message - {}"
                              .format(e.message))

    def run(self):
        self.amqp_channel.basic_consume(self._callback,
                                        queue=QUEUE,
                                        no_ack=True)
        self.amqp_channel.start_consuming()


def _create_amqp_channel():
    host = CONF.get("amqp", "host")
    port = CONF.get("amqp", "port")
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host,
        port=port))
    return connection.channel()


