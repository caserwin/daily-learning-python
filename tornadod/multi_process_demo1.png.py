#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-09 11:22
# @Author  : erwin
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json
import time


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        start = time.time()
        time.sleep(10)
        raw_data = {
            "start time": int(start),
            "message": "Hello World!!",
            "run time": time.time() - start
        }
        self.write(json.dumps(raw_data))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/index", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.bind(8000)
    http_server.start(0)
    print("start")
    tornado.ioloop.IOLoop.instance().start()
