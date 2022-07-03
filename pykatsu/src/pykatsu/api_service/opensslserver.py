from .externalservice import ExternalService
from .openssl import OPENSSL_BIN_PATH
from .opensslkeys import CRT_PATH, KEY_PATH


class OpenSslServer(ExternalService):
    def __init__(self, port):
        super().__init__()
        self.port = port

    @property
    def cmd(self):
        return [
            str(OPENSSL_BIN_PATH),
            's_server',
            '-debug',
            f'-cert={CRT_PATH}',
            f'-key={KEY_PATH}',
            f'-accept={self.port}',
            ]

    @property
    def expected_startup_time(self):
        return 0.5
