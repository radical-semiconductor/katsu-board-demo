import pytest

from .externalservice import ExternalService
from .test_helpers import process_is_running


class DummyYesService(ExternalService):
    @property
    def cmd(self):
        return ['yes', 'radical']

    @property
    def expected_startup_time(self):
        return 0.1

@pytest.fixture
def service():
    s = DummyYesService()
    yield s
    s.stop()

def dummy_service_running():
    return process_is_running('yes', required_args=['radical'])

def test_unstarted_service_has_no_pid(service):
    assert service.pid is None

def test_can_start_service(service):
    assert not dummy_service_running()
    service.ensure_started()
    assert dummy_service_running()

def test_can_stop_service(service):
    service.ensure_started()
    service.stop()
    assert not dummy_service_running()

def test_ensure_started_leaves_running_instance_running(service):
    service.ensure_started()
    old_pid = service.pid
    service.ensure_started()
    assert old_pid == service.pid

def test_ensure_started_restarts_if_previously_running_crashes(service):
    service.ensure_started()
    assert dummy_service_running()
    import os
    import signal

    # kill via outside channel
    os.kill(service.pid, signal.SIGKILL)
    assert not dummy_service_running()
    service.ensure_started()
    assert dummy_service_running()

def test_can_report_status(service):
    assert dummy_service_running() == service.running()
    service.ensure_started()
    assert dummy_service_running() == service.running()

def test_service_can_be_read(service):
    service.ensure_started()
    assert service.read(2) == "radical\nradical\n"

def test_unstarted_service_can_be_read_as_empty(service):
    assert service.read(2) == ""
