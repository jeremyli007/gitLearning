#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/8/16 21:34
# software: PyCharm
#!/usr/bin/env python # coding=utf-8
"""
the url structure of website
"""
import sys
#utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")
from .handlers.index import IndexHandler #假设已经有了
url = [
    (r'/', IndexHandler),
]