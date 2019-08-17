#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/8/16 21:59
# software: PyCharm

import tornado.web
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")