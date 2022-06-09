import datetime

from flask import Flask, jsonify

import opensslkeys
from app import app
from opensslserver import OpenSslServer


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/api/timestamp')
def time():
    ts = str(datetime.datetime.now())
    return jsonify({'time': ts})

@app.route('/api/keys/generate')
def keys_generate():
    opensslkeys.ensure_generated()
    return jsonify({'success': True})

@app.route('/api/keys/purge')
def keys_purge():
    opensslkeys.purge()
    return jsonify({'success': True})

@app.route('/api/keys/list')
def keys_list():
    keys = opensslkeys.list_keys()
    return jsonify({'keys': keys})

_server = OpenSslServer()
@app.route('/api/server/start')
def server_start():
    try:
        _server.ensure_started()
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})

@app.route('/api/server/stop')
def server_stop():
    _server.stop()
    return jsonify({'success': True})

@app.route('/api/server/status')
def server_status():
    return jsonify(
        running=_server.running(),
    )
