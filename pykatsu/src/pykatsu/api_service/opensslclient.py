from .externalservice import ExternalService


class OpenSslClient(ExternalService):
    def __init__(self, port):
        super().__init__()
        self.port = port

    @property
    def cmd(self):
        return [
            'openssl',
            's_client',
            f'-connect=localhost:{self.port}',
            '-tls1_3',
            ]

    @property
    def expected_startup_time(self):
        return 0.01
