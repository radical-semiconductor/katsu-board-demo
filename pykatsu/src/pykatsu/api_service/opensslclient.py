from .externalservice import ExternalService
from pykatsu.projectpath import  KATSU_PROJECT_ROOT


class OpenSslClient(ExternalService):
    def __init__(self, port):
        super().__init__()
        self.port = port

    @property
    def cmd(self):
        return [
            str(KATSU_PROJECT_ROOT / 'openssl' / 'apps' / 'openssl'),
            's_client',
            '-debug',
            f'-connect=localhost:{self.port}',
            ]

    @property
    def expected_startup_time(self):
        return 0.01
