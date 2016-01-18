import logging

from daemonize import Daemonize
from sonic_client.sonic_client import SonicClient

pid = "/tmp/sonic.pid"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
fh = logging.FileHandler("/var/log/sonic_client/sonic_client.log", "w")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]


def app():
    SonicClient(logger).run()

def main():
    logger.debug("Starting sonic client")
    daemon = Daemonize(app="sonic_client", pid=pid, action=app, keep_fds=keep_fds)
    daemon.start()

if __name__ == "__main__":
    main()
