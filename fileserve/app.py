#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask, Response, request
from flask_restful import Api, Resource
import xlwt

app = Flask(__name__)
api = Api(app)

class FileDownload(Resource):
    def post(self):
        book = xlwt.Workbook()
        booksheet = book.add_sheet('sheet 1', cell_overwrite_ok=True)

        #将thead分为两个数组，一个是关键字，一个是标题
        try:
            data = request.get_json()
            hkeys = data['columns']
            htitle = data['fields'] 
            items = data['items']
            for col in xrange(len(hkeys)):
                booksheet.write(0, col, htitle[col])
            for row in xrange(len(items)):
                for col in xrange(len(hkeys)):
                    booksheet.write(row+1, col, items[row][hkeys[col]])
        except BaseException as e:
            #self.logger.error(str(e))
            print "Error:",e
        #except:
            booksheet.write(0, 0, 'Request Error!')

        rsp=Response(mimetype='application/vnd.ms-excel')
        rsp.headers['filename']=('default.xls').encode('utf8')
        book.save(rsp.stream)
        return rsp

api.add_resource(FileDownload, '/download')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8173, debug=True)
