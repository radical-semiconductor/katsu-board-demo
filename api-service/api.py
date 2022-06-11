import datetime

from flask import jsonify

import opensslkeys
from app import app
from mcpservice import MCPService
from opensslserver import OpenSslServer


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/api/timestamp')
def time():
    ts = str(datetime.datetime.now())
    return jsonify(time=ts)

@app.route('/api/keys/generate')
def keys_generate():
    opensslkeys.ensure_generated()
    return jsonify(success=True)

@app.route('/api/keys/purge')
def keys_purge():
    opensslkeys.purge()
    return jsonify(success=True)

@app.route('/api/keys/list')
def keys_list():
    keys = opensslkeys.list_keys()
    return jsonify(keys=keys)

ECHO_DEMO_PORT=9898
_server = OpenSslServer(ECHO_DEMO_PORT)
@app.route('/api/server/start')
def server_start():
    try:
        _server.ensure_started()
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/api/server/stop')
def server_stop():
    _server.stop()
    return jsonify(success=True)

@app.route('/api/server/status')
def server_status():
    return jsonify(
        running=_server.running(),
    )

_client = OpenSslClient(ECHO_DEMO_PORT)
@app.route('/api/client/start')
def client_start():
    try:
        _client.ensure_started()
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/api/client/stop')
def client_stop():
    _client.stop()
    return jsonify(success=True)

@app.route('/api/client/status')
def client_status():
    return jsonify(
        running=_client.running(),
    )

_mcp = MCPService()
@app.route('/api/mcp/start')
def mcp_start():
    try:
        _mcp.ensure_started()
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/api/mcp/stop')
def mcp_stop():
    _mcp.stop()
    return jsonify(success=True)

@app.route('/api/mcp/status')
def mcp_status():
    return jsonify(
        running=_mcp.running(),
    )

@app.route('/api/mcp/diagnostic')
def mcp_diagnostic():
    return jsonify(message=_mcp.do_diagnostic(9))
