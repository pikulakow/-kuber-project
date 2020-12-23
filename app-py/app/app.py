import os
import json

from flask import Flask
app = Flask(__name__)

@app.route("/health")
def health():
    return '{"status": "OK"}'

@app.route("/")
def hello():
    return 'Simple python service v.1'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='80')
