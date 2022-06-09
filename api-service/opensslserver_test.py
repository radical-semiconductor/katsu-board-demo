import pytest

import opensslkeys
from opensslserver import OpenSslServer
from test_helpers import process_is_running


@pytest.fixture
def openssl_server():
    opensslkeys.ensure_generated()
    s = OpenSslServer()
    yield s
    s.stop()

def test_server_cant_start_without_keys(openssl_server:OpenSslServer):
    opensslkeys.purge()
    with pytest.raises(RuntimeError, match="Failed to start `openssl"):
        openssl_server.ensure_started()
