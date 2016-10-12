#! /usr/bin/env python
# coding=UTF-8

from flask import Flask
from bg import bg
from vote import vote

app = Flask(__name__)
app.register_blueprint(bg.app)
app.register_blueprint(vote.app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2553, debug=True)
