from flask import send_from_directory

from app import app

@app.route('/')
def start_frontend():
    return send_from_directory("../frontend/bin/Debug/net6.0/publish/wwwroot", "index.html")

@app.route('/<path:path>')
def serve_frontend_assets(path):
    return send_from_directory("../frontend/bin/Debug/net6.0/publish/wwwroot", path)
