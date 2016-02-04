import ConfigParser


class Config(object):
    def __init__(self):
        conf = ConfigParser.RawConfigParser()
        conf.read("/etc/sonic_client/sonic_client.conf")

        # client related parameters
        self.salt = conf.get("client", "salt")
        self.name = conf.get("client", "name")
        self.uuid = conf.get("client", "uuid")

        # amqp related parameters
        self.amqp_host = conf.get("amqp", "host")
        self.amqp_port = conf.getint("amqp", "port")
        self.amqp_username = conf.get("amqp", "username")
        self.amqp_password = conf.get("amqp", "password")
        self.app_queue = conf.get("amqp", "app_queue")

CONF = Config()
