import datetime;

from flask import Flask, jsonify

from app import app

@app.route('/api/timestamp')
def time():
    ts = str(datetime.datetime.now())
    return jsonify({'time': ts})
