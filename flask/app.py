#!/usr/bin/python
# coding=UTF-8

from flask import Flask
from flask import request
from flask import jsonify, make_response
import json

app = Flask(__name__)

@app.route('/api/v1/hw/', methods=['GET'])
def hw():
    return 'Hello World'

@app.route('/api/v1/test/', methods=['GET', 'POST'])
def test():
    # request.form 只能拿到 POST or PUT or GET or DELETE 方法中**表单**的数据
    if request.method == 'POST':
        rs = request.get_json()
        with open('tx','w') as fp:
            json.dump(rs, fp)
        return make_response(jsonify(rs))
    # request.args 只能拿到URL中'?'号后的参数
    elif request.method == 'GET':
        rs = request.args.get('key', 'GET')
        return rs
    else:
        return 'NOT ALLOWED'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2553, debug=True)
