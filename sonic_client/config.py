import ConfigParser


class Config(object):
    def __init__(self):
        conf = ConfigParser.RawConfigParser()
        conf.read("/etc/sonic_client/sonic_client.conf")

        # client related parameters
        self.salt = conf.get("client", "salt")
        self.name = conf.get("client", "name")

        # amqp related parameters
        self.amqp_host = conf.get("amqp", "host")
        self.amqp_port = conf.getint("amqp", "port")
        self.amqp_username = conf.getint("amqp", "username")
        self.amqp_password = conf.getint("amqp", "password")

CONF = Config()
