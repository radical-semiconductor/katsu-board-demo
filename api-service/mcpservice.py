import sys

from externalservice import ExternalService

sys.path.insert(1, '../mcp-mock/mcp-mock')
import socket

import mcp_pb2
import util


class MCPService(ExternalService):
    @property
    def cmd(self):
        return ['../start.mcp-mock.sh']

    @property
    def expected_startup_time(self):
        return 3

    def _run_command(self, command, response_cls):
        # connect to the MCP
        mcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mcp_sock.connect(("localhost", 1337))

        # send the command
        command_data = command.SerializeToString()
        util.send_length_prefix_data(mcp_sock, command_data)

        # receive the response
        response_data = util.receive_length_prefix_data(mcp_sock)

        # deserialize response
        response = response_cls().FromString(response_data)
        return response

    def do_diagnostic(self, diagnostic_num):
        """Perform a diagnostic test:  diagnostic 4"""
        command = mcp_pb2.Command(
            diagnostic=mcp_pb2.DiagnosticCommand(diagnostic=diagnostic_num)
        )
        response = self._run_command(command, mcp_pb2.DiagnosticResponse)
        if response.success:
            return "Diagnostic passed."
        else:
            return f'Diagnostic failed with error: "{response.error}".'
