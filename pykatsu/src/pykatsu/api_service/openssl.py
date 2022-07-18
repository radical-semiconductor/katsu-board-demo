import os
import sys

from pykatsu.projectpath import KATSU_PROJECT_ROOT

OPENSSL_ROOT_PATH = KATSU_PROJECT_ROOT / 'openssl-output'
OPENSSL_BIN_PATH = OPENSSL_ROOT_PATH / 'bin' / 'openssl'
OPENSSL_CONFIG_PATH = OPENSSL_ROOT_PATH / 'ssl' / 'openssl.cnf'

if sys.platform.startswith('win') or str(sys.executable).lower().endswith('exe'):
    OPENSSL_BIN_PATH = OPENSSL_BIN_PATH.with_suffix('.exe')

if not OPENSSL_BIN_PATH.exists():
    print(f"Warning, openssl binary doesn't exist at `{str(OPENSSL_BIN_PATH)}`")

OPENSSL_ENV = os.environ.copy()
OPENSSL_ENV["OPENSSL_CONF"] = str(OPENSSL_CONFIG_PATH)
