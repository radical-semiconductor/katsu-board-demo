import opensslkeys


def test_can_create_keys():
    opensslkeys.ensure_generated()
    assert opensslkeys.KEY_PATH.exists()
    assert opensslkeys.CRT_PATH.exists()

def test_can_purge_keys():
    opensslkeys.ensure_generated()
    opensslkeys.purge()
    assert not opensslkeys.KEY_PATH.exists()
    assert not opensslkeys.CRT_PATH.exists()
