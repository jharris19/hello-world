import os
from flask import Flask


app = Flask(__name__)


def hello(name):
    return f"hello, {name}!"


@app.route("/")
def hello_world():
    return f"<p>{hello(os.getenv('HELLO_NAME', 'pyCharm'))}</p>"
