from externalservice import ExternalService


class MCPService(ExternalService):
    @property
    def cmd(self):
        return ['../start.mcp-mock.sh']

    @property
    def expected_startup_time(self):
        return 3
