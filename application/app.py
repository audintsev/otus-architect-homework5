import os

from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health():
    return '{"status": "OK"}'


@app.route("/version")
def version():
    return '{"version": "0.1"}'


@app.route("/")
def hello():
    return '{"message": "Hello world from ' + os.environ['HOSTNAME'] + '!"}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
