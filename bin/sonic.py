import logging

from daemon import runner
from sonic_client.sonic_client import SonicClient

pid = "/var/run/sonic_client/sonic.pid"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
log_path = "/var/log/sonic_client/sonic_client.log"
fh = logging.FileHandler(log_path, "w")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]


class App:
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = pid
        self.pidfile_timeout = 5

    def run(self):
        SonicClient(logger).run()


app = App()


def main():
    logger.debug("Starting sonic client")
    daemon_runner = runner.DaemonRunner(app)
    daemon_runner.daemon_context.files_preserve = [fh.stream]
    daemon_runner.daemon_context.initgroups = False
    daemon_runner.do_action()


if __name__ == "__main__":
    main()
