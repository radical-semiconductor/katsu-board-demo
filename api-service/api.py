import datetime

from flask import Flask, jsonify

import opensslkeys
from app import app
from opensslserver import OpenSslServer


@app.route('/api/timestamp')
def time():
    ts = str(datetime.datetime.now())
    return jsonify({'time': ts})

@app.route('/api/keys/generate')
def keys_generate():
    opensslkeys.ensure_generated()

@app.route('/api/keys/purge')
def keys_purge():
    opensslkeys.purge()

@app.route('/api/keys/list')
def keys_list():
    keys = opensslkeys.list_keys()
    return jsonify({'keys': keys})

_server = OpenSslServer()
@app.route('/api/server/start')
def server_start():
    _server.ensure_started()

@app.route('/api/server/stop')
def server_stop():
    _server.stop()
