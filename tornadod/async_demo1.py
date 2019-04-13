#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-09 13:35
# @Author  : erwin
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.gen
from tornado.options import options, define
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
import time
import json

define("port", default=8001, help="跑在8001", type=int)


class SleepHandler(tornado.web.RequestHandler):
    # 起线程池，由当前RequestHandler持有
    executor = ThreadPoolExecutor(20)

    @tornado.gen.coroutine
    def get(self):
        # 使用yield得到了一个生成器，先把流程挂起，等完全完毕，再唤醒继续执行。另，生成器都是异步的。
        raw_data = yield self.block_task(10)
        self.write(json.dumps(raw_data))

    @run_on_executor
    def block_task(self, stime):
        start = time.time()
        time.sleep(stime)
        raw_data = {
            "start time": int(start),
            "message": "SleepHandler Hello World!!",
            "run time": time.time() - start
        }
        return raw_data


class DirectHandler(tornado.web.RequestHandler):
    def get(self):
        start = time.time()
        time.sleep(10)
        raw_data = {
            "start time": int(start),
            "message": "DirectHandler Hello World!!",
            "run time": time.time() - start
        }
        self.write(json.dumps(raw_data))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/d", DirectHandler),
            (r"/s", SleepHandler),
        ],
        debug=False
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(1)
    print("start")
    tornado.ioloop.IOLoop.instance().start()
