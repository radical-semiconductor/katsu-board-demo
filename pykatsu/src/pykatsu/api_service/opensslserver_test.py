import pytest

from . import opensslkeys
from .opensslserver import OpenSslServer
from .test_helpers import process_is_running


@pytest.fixture(scope='session')
def openssl_server():
    opensslkeys.ensure_generated()
    s = OpenSslServer(5555)
    yield s
    s.stop()

@pytest.mark.openssl
def test_server_can_start(openssl_server:OpenSslServer):
    openssl_server.ensure_started()
    assert process_is_running('openssl', required_args=['s_server'])

@pytest.mark.openssl
def test_server_cant_start_without_keys():
    opensslkeys.purge()
    with pytest.raises(RuntimeError, match="Failed to start `.*openssl"):
        OpenSslServer(5555).ensure_started()
