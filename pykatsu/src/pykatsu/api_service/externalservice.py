import atexit
import subprocess
import time
from queue import Empty, Queue
from threading import Thread

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

        self._process = subprocess.Popen(
            self.cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1, # line buffered
            )

        self.set_up_io_queue()

        try:
            # see if external service stays started
            self._process.wait(self.expected_startup_time)
            raise RuntimeError(f"Failed to start `{' '.join(self.cmd)}`\n{''.join(self.read(100))}")
        except subprocess.TimeoutExpired:
            pass

    def set_up_io_queue(self):
        self.stdout_q = Queue(maxsize=4000)
        def enqueue_stdout():
            for line in iter(self._process.stdout.readline, ""):
                self.stdout_q.put(line)
        Thread(
            target=enqueue_stdout,
            daemon=True,
            ).start()


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

    def read(self, n):
        "Read at most n lines of output if availble."
        if self._process is None:
            return ""

        lines = []
        try:
            for _ in range(n):
                lines.append(self.stdout_q.get_nowait())
        except Empty:
            # out of lines
            pass

        return "".join(lines)
