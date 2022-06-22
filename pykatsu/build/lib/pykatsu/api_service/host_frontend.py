from flask import redirect, send_from_directory, url_for

from .flaskapp import app


@app.route('/')
def start_frontend():
    return send_from_directory("../frontend/bin/Debug/net6.0/publish/wwwroot", "index.html")

@app.route('/<path:path>')
def serve_frontend_assets(path):
    return send_from_directory("../frontend/bin/Debug/net6.0/publish/wwwroot", path)

@app.errorhandler(404)
def redirect_back_to_blazor_startup(e):
    return redirect(url_for('start_frontend'), code=301)
