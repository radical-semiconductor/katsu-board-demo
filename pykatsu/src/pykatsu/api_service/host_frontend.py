import os

from flask import redirect, send_from_directory, url_for

from ..projectpath import KATSU_PROJECT_ROOT
from .flaskapp import app

FRONTEND_BLAZOR_OUTPUT_PATH = KATSU_PROJECT_ROOT / "frontend-blazor-output" / "wwwroot"
if FRONTEND_BLAZOR_OUTPUT_PATH.exists():
    print("Serving frontend-blazor using flask.\n")
    @app.route('/')
    def start_frontend():
        return send_from_directory(FRONTEND_BLAZOR_OUTPUT_PATH, "index.html")

    @app.route('/<path:path>')
    def serve_frontend_assets(path):
        return send_from_directory(FRONTEND_BLAZOR_OUTPUT_PATH, path)

    @app.errorhandler(404)
    def redirect_back_to_blazor_startup(e):
        return redirect(url_for('start_frontend'), code=301)
else:
    print(
        "Not serving frontend-blazor using flask.",
        "Either you are a developer and running frontend-blazor separately.",
        "Otherwise something went wrong, please contact support.",
        sep='\n')
