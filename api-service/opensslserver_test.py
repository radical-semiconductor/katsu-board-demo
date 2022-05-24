import pytest

import opensslkeys
from opensslserver import OpenSslServer
from test_helpers import process_is_running


@pytest.fixture
def server():
    opensslkeys.ensure_generated()
    s = OpenSslServer()
    yield s
    s.stop()

def openssl_s_server_running():
    return process_is_running('openssl', required_args=['s_server'])

def test_unstarted_server_has_no_pid(server):
    assert server.pid is None

def test_server_cant_start_without_keys():
    opensslkeys.purge()
    assert not openssl_s_server_running()

def test_can_start_openssl_server(server):
    assert not openssl_s_server_running()
    server.ensure_started()
    assert openssl_s_server_running()

def test_can_stop_openssl_server(server):
    server.ensure_started()
    server.stop()
    assert not openssl_s_server_running()

def test_ensure_started_leaves_running_instance_running(server):
    server.ensure_started()
    old_pid = server.pid
    server.ensure_started()
    assert old_pid == server.pid

def test_ensure_started_restarts_if_previously_running_crashes(server):
    server.ensure_started()
    assert openssl_s_server_running()
    import os
    import signal

    # kill via outside channel
    os.kill(server.pid, signal.SIGKILL)
    assert not openssl_s_server_running()
    server.ensure_started()
    assert openssl_s_server_running()

def test_can_report_status(server):
    assert openssl_s_server_running() == server.running()
    server.ensure_started()
    assert openssl_s_server_running() == server.running()
