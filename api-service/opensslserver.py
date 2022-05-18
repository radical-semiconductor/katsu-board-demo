import atexit
import subprocess


class OpenSslServer:
    def __init__(self):
        self._process = None

        # Clean up server if python closes
        atexit.register(self.stop)

    @property
    def pid(self):
        if self._process is None:
            return None
        return self._process.pid

    def running(self):
        if self._process is None:
            return False
        if self._process.poll() is None:
            return True
        else:
            return False

    def ensure_started(self):
        if self.running():
            return

        self._process = subprocess.Popen([
            'openssl',
            's_server',
            '-cert=../radical.crt',
            '-key=../radical.key',
            '-accept=8888',
            ])

    def stop(self):
        if self._process is None:
            return

        if not self.running():
            # died or killed by outside means
            self._process = None
            return

        self._process.terminate()
        try:
            # wait for upto 5 seconds for graceful shutdown
            self._process.wait(5)
        except subprocess.TimeoutExpired:
            self._process.kill()
        self._process = None
