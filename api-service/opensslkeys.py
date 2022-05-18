import os
import subprocess
from pathlib import Path

KEY_PATH = Path('../radical.key')
CRT_PATH = KEY_PATH.with_suffix('.crt')

def ensure_generated():
    if KEY_PATH.exists() and CRT_PATH.exists():
        return
    # generate private key and self signed cert
    subprocess.run([
        'openssl',
        'req',
        '-x509',
        '-newkey=rsa:4096', # also generate key
        '-nodes', # no password for key
        f'-keyout={KEY_PATH}',
        f'-out={CRT_PATH}',
        '-subj=/C=US/ST=Oregon/L=Portland/O=Company Name/OU=Org/CN=www.example.com',
        ])

def purge():
    os.remove(KEY_PATH)
    os.remove(CRT_PATH)

def list_keys():
    keys = []
    if KEY_PATH.exists:
        keys.append(KEY_PATH.name)
    if CRT_PATH.exists:
        keys.append(CRT_PATH.name)
    return keys
