#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/8/16 21:34
# software: PyCharm
from .url import url
import tornado.web
import os
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "template"),
    static_path = os.path.join(os.path.dirname(__file__), "statics")
    )
application = tornado.web.Application(
    handlers = url, **settings
)