import pytest

from .mcpservice import MCPService
from .test_helpers import process_is_running


@pytest.fixture(scope='session')
def mcp_service():
    s = MCPService()
    yield s
    s.stop()

def test_mcp_can_start(mcp_service:MCPService):
    mcp_service.ensure_started()
    assert process_is_running('python', required_args=['pykatsu.mcp_mock.mcp', '1337'])
