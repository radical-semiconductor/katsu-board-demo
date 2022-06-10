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

    @property
    def expected_startup_time(self):
        # dev machine took about 0.001 before failing out
        # with missing keys
        # give margin of safety
        return 0.01
