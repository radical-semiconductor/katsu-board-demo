import os
import subprocess
from pathlib import Path

from pykatsu.projectpath import KATSU_PROJECT_ROOT

from .openssl import OPENSSL_BIN_PATH, OPENSSL_ENV

KEY_PATH = Path(f'{KATSU_PROJECT_ROOT}/radical.key')
CRT_PATH = KEY_PATH.with_suffix('.crt')

def ensure_generated():
    if KEY_PATH.exists() and CRT_PATH.exists():
        return
    # generate private key and self signed cert
    subprocess.run([
        str(OPENSSL_BIN_PATH),
        'req',
        '-x509',
        '-newkey=rsa:4096', # also generate key
        '-nodes', # no password for key
        f'-keyout={KEY_PATH}',
        f'-out={CRT_PATH}',
        '-subj=/C=US/ST=Oregon/L=Portland/O=Company Name/OU=Org/CN=localhost',
        ],
        env=OPENSSL_ENV,
        )

def purge():
    for p in [KEY_PATH, CRT_PATH]:
        try:
            os.remove(p)
        except FileNotFoundError:
            pass

def list_keys():
    keys = []
    if KEY_PATH.exists():
        keys.append(KEY_PATH.name)
    if CRT_PATH.exists():
        keys.append(CRT_PATH.name)
    return keys
