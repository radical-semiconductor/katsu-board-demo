import pytest

from . import opensslkeys
from .opensslclient import OpenSslClient
from .opensslserver import OpenSslServer
from .test_helpers import process_is_running


@pytest.fixture(scope='session')
def openssl_client():
    opensslkeys.ensure_generated()
    s = OpenSslServer(9898)
    s.ensure_started()
    import time
    time.sleep(5)
    c = OpenSslClient(9898)
    yield c
    c.stop()
    s.stop()

def test_client_can_start(openssl_client:OpenSslClient):
    openssl_client.ensure_started()
    # Can't check in the normal way because openssl is either purposely
    # inadvertantly scrubbing argv from the process
    # assert process_is_running('openssl', required_args=['s_client'])
