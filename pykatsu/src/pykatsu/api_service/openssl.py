import os
import subprocess

from pykatsu.projectpath import KATSU_PROJECT_ROOT

OPENSSL_ROOT_PATH = KATSU_PROJECT_ROOT / 'openssl'
OPENSSL_BIN_PATH = OPENSSL_ROOT_PATH / 'apps' / 'openssl'
OPENSSL_ENV = os.environ.copy()
OPENSSL_ENV["OPENSSL_CONF"] = str(OPENSSL_ROOT_PATH / 'apps'/ 'openssl.cnf')
