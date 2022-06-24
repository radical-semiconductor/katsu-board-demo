import pytest

from . import opensslkeys
from .opensslclient import OpenSslClient
from .opensslserver import OpenSslServer
from .test_helpers import process_is_running


@pytest.fixture(scope='session')
def openssl_client_server():
    opensslkeys.ensure_generated()
    port = 15000
    s = OpenSslServer(port)
    s.ensure_started()
    import time
    time.sleep(1)
    c = OpenSslClient(port)
    yield c, s
    c.stop()
    s.stop()

def test_client_can_start(openssl_client_server):
    c, s = openssl_client_server
    try:
        c.ensure_started()
    except Exception as e:
        print("Client connection failed.")
        print("Below is output from server side:")
        print(s.read(200))
        raise e
    # Can't check in the normal way because openssl is either purposely
    # inadvertantly scrubbing argv from the process
    # assert process_is_running('openssl', required_args=['s_client'])
