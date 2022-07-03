import os

from pykatsu.projectpath import KATSU_PROJECT_ROOT

OPENSSL_ROOT_PATH = KATSU_PROJECT_ROOT / 'openssl-output'
OPENSSL_BIN_PATH = OPENSSL_ROOT_PATH / 'bin' / 'openssl'
OPENSSL_CONFIG_PATH = OPENSSL_ROOT_PATH / 'ssl' / 'openssl.cnf'

OPENSSL_ENV = os.environ.copy()
OPENSSL_ENV["OPENSSL_CONF"] = str(OPENSSL_CONFIG_PATH)
