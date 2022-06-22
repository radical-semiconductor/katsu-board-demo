from .externalservice import ExternalService


class OpenSslServer(ExternalService):
    def __init__(self, port):
        super().__init__()
        self.port = port

    @property
    def cmd(self):
        return [
            'openssl',
            's_server',
            '-cert=../radical.crt',
            '-key=../radical.key',
            f'-accept={self.port}',
            ]

    @property
    def expected_startup_time(self):
        # dev machine took about 0.001 before failing out
        # with missing keys
        # give margin of safety
        return 0.01
