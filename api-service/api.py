import datetime

from flask import Flask, jsonify

import opensslkeys
from app import app
from opensslserver import OpenSslServer


@app.route('/api/timestamp')
def time():
    ts = str(datetime.datetime.now())
    return jsonify({'time': ts})

@app.route('api/keys/generate')
def generate_keys():
    opensslkeys.ensure_generated()

_server = OpenSslServer()
@app.route('api/server/start')
def generate_keys():
    _server.ensure_started()
