import json
import traceback

from config import CONF
from manager import Manager
from amqp_client import AmqpClient


class ActionUnsupportedError(Exception):
    def __init__(self, action):
        super(Exception, self).__init__("{} action is not"
                                        "supported by sonic"
                                        "client".format(action))


class SonicClient(object):
    QUEUE = CONF.uuid

    def __init__(self, logger):
        self.amqp_client = AmqpClient()
        self.manager = Manager(self.amqp_client)
        self.logger = logger

    def _callback(self, ch, method, properties, body):
        self.logger.debug("Processing {}".format(body))
        try:
            # message = json.loads(decrypt(body))
            message = json.loads(body)
            for key, val in message.iteritems():
                if hasattr(self.manager, key):
                    getattr(self.manager, key)(val)
                else:
                    raise ActionUnsupportedError(key)
        except Exception as e:
            self.logger.error("Error while processing message - {0}\n{1}"
                              .format(e.message, traceback.format_exc()))

    def run(self):
        self.logger.debug("Starting sonic client")
        try:
            self.amqp_client.channel.queue_declare(queue=self.QUEUE)
            self.amqp_client.channel.basic_consume(self._callback,
                                                   queue=self.QUEUE,
                                                   no_ack=True)
            self.amqp_client.channel.start_consuming()
        except Exception as e:
            self.logger.error("Error in connecting to rabbit server - {0}\n{1}"
                              .format(e.message, traceback.format_exc()))

