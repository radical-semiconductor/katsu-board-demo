from flask import Flask

app = Flask(__name__)
from . import api, host_frontend
