import pytest

from . import opensslkeys


@pytest.mark.openssl
def test_can_create_keys():
    opensslkeys.ensure_generated()
    assert opensslkeys.KEY_PATH.exists()
    assert opensslkeys.CRT_PATH.exists()

@pytest.mark.openssl
def test_can_purge_keys():
    opensslkeys.ensure_generated()
    opensslkeys.purge()
    assert not opensslkeys.KEY_PATH.exists()
    assert not opensslkeys.CRT_PATH.exists()

@pytest.mark.openssl
def test_can_purge_is_idempotent():
    opensslkeys.purge()
    opensslkeys.purge()

@pytest.mark.openssl
def test_can_list_keys():
    opensslkeys.ensure_generated()
    keys = opensslkeys.list_keys()
    assert keys == [
        'radical.key',
        'radical.crt',
        ]

@pytest.mark.openssl
def test_can_list_no_keys():
    opensslkeys.purge()
    keys = opensslkeys.list_keys()
    assert keys == [
        ]
