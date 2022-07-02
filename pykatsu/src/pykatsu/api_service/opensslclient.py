from .externalservice import ExternalService
from .openssl import OPENSSL_BIN_PATH


class OpenSslClient(ExternalService):
    def __init__(self, port):
        super().__init__()
        self.port = port

    @property
    def cmd(self):
        return [
            str(OPENSSL_BIN_PATH),
            's_client',
            '-debug',
            f'-connect=localhost:{self.port}',
            ]

    @property
    def expected_startup_time(self):
        return 0.01
