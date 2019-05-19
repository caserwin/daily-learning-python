#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-01 10:13
# @Author  : erwin
import time
import tornado.web
from tornado.ioloop import IOLoop


def blocking_func(t):
    time.sleep(t)
    return t


class asyncMainHandler(tornado.web.RequestHandler):
    async def get(self):
        start = int(time.time())
        res = await IOLoop.current().run_in_executor(None, blocking_func, 10)
        self.write({"start time": start, "run time": res})


class syncMainHandler(tornado.web.RequestHandler):
    def get(self):
        start = int(time.time())
        res = blocking_func(10)
        self.write({"start time": start, "run time": res})


application = tornado.web.Application([
    (r"/sync", syncMainHandler),
    (r"/async", asyncMainHandler),
])

if __name__ == "__main__":
    application.listen(8001)
    print('server start')
    IOLoop.current().start()
