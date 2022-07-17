import os
import webbrowser

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
from . import api, host_frontend

try:
    FLASK_RUN_PORT = int(os.environ['FLASK_RUN_PORT'])
    webbrowser.open(f'http://127.0.0.1:{FLASK_RUN_PORT}/')
except:
    print("Error while trying to open app in a browser.")
    # We are also expected to get here when using the standard
    # development scripts, the browser is opened by blazor dev loop
