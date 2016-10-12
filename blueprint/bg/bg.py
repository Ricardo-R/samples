#!/usr/bin/python
# coding=UTF-8

from flask import Blueprint
from flask import request
from flask import jsonify, make_response
import json

app = Blueprint(__name__+'Mod', __name__) 

def _transit(src, order=1):
    rs = {}
    # [] to {}
    if order == 1:
        for item in src['items']:
            rs[item['id']] = item;
        return rs
    # {} to []
    else:
        rs['items'] = []
        for item in src:
            rs['items'].append(src[item])
        return rs
def _getall():
    resp = {"items":[]}
    try:
        with open(__name__+'File', 'r') as fp:
            rsload = json.load(fp)
            resp = _transit(rsload, 2)
            return make_response(jsonify(resp))
    except:
        return make_response(jsonify(resp))


@app.route('/api/v1/bg/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def sys():
    # 返回格式 {"items":[{"id":"ssx", "order":"xxx"},]}
    if request.method == 'GET':
        return _getall()
    else:
        if request.method == 'POST':
            req = request.get_json()
            rsload = {}
            if req["trigger"] == 'on':
                with open(__name__+'File', 'w') as fp:
                    pass
                return _getall()
            try:
                with open(__name__+'File', 'r') as fp:
                    rsload = json.load(fp)
            except:
                pass
            for item in req['items']:
                rsload[item['id']] = item
            with open(__name__+'File', 'w') as fp:
                json.dump(rsload, fp)
            return _getall()
        else:
            response = {"ERROR":"METHOD NOT ALLOWED"}
            return make_response(jsonify(response))

if __name__ == '__main__':
    from flask import Flask
    webapp = Flask('bgsys')
    webapp.register_blueprint(app)
    webapp.run(host='127.0.0.1', port=2553, debug=True)
