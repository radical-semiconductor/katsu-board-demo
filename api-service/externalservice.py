import atexit
import subprocess

import psutil


class ExternalService:
    def __init__(self):
        self._process = None

        # Clean up server if python closes
        atexit.register(self.stop)

    @property
    def cmd(self):
        raise NotImplementedError

    @property
    def expected_startup_time(self):
        raise NotImplementedError

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

        self._process = subprocess.Popen(self.cmd)
        try:
            # see if external service stays started
            self._process.wait(self.expected_startup_time)
            raise RuntimeError(f"Failed to start `{' '.join(self.cmd)}`")
        except subprocess.TimeoutExpired:
            return

    def stop(self):
        if self._process is None:
            return

        if not self.running():
            # died or killed by outside means
            self._process = None
            return

        parent = psutil.Process(self.pid)
        children = [c for c in parent.children(recursive=True)]
        for p in children + [parent]:
            p.terminate()
            try:
                # wait for upto 5 seconds for graceful shutdown
                p.wait(5)
            except psutil.TimeoutExpired:
                p.kill()

        self._process = None
