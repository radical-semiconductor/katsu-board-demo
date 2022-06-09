from externalservice import ExternalService


class OpenSslServer(ExternalService):
    @property
    def cmd(self):
        return [
            'openssl',
            's_server',
            '-cert=../radical.crt',
            '-key=../radical.key',
            '-accept=8888',
            ]
