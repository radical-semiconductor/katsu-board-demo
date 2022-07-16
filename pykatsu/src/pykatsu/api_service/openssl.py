import os
import sys

from pykatsu.projectpath import KATSU_PROJECT_ROOT

OPENSSL_ROOT_PATH = KATSU_PROJECT_ROOT / 'openssl-output'
if sys.platform.startswith('linux'):
    OPENSSL_BIN_PATH = OPENSSL_ROOT_PATH / 'bin' / 'openssl'
    OPENSSL_CONFIG_PATH = OPENSSL_ROOT_PATH / 'ssl' / 'openssl.cnf'
elif sys.platform.startswith('darwin'):
    OPENSSL_BIN_PATH = OPENSSL_ROOT_PATH / 'bin' / 'openssl'
    OPENSSL_CONFIG_PATH = OPENSSL_ROOT_PATH / 'ssl' / 'openssl.cnf'
elif sys.platform.startswith('win') or str(sys.executable).lower().endswith('exe'):
    OPENSSL_BIN_PATH = OPENSSL_ROOT_PATH / 'Program Files' / 'OpenSSL' / 'bin' / 'openssl.exe'
    OPENSSL_CONFIG_PATH = OPENSSL_ROOT_PATH / 'Program Files' / 'Common Files' / 'SSL' / 'openssl.cnf'
else:
    raise NotImplementedError("Unknown platform. Unable to know path to openssl binaries")

if not OPENSSL_BIN_PATH.exists():
    print(f"Warning, openssl binary doesn't exist at `{str(OPENSSL_BIN_PATH)}`")

OPENSSL_ENV = os.environ.copy()
OPENSSL_ENV["OPENSSL_CONF"] = str(OPENSSL_CONFIG_PATH)
