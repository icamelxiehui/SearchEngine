#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-05-27 15:07:19
@author xiehui
"""
import os
import sys

ROOT_DIR = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
reload(sys)     
sys.setdefaultencoding('utf8')
sys.path.append(ROOT_DIR)

import lib.path
lib.path.create_path("ROOT_DIR", ROOT_DIR)

from framework import Framework
from flask import Flask,request  

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def process():
    query = request.args.get("query","")
    framework = Framework()
    return framework.process(query)

if __name__ == "__main__":
    #framework = Framework()
    #framework.start()
    #print framework.process("中金云网无双科技+10.1%~20%  a")
    #print framework.process("中国船舶+1.2,1.3,12:30:40,2019.5.30,5+2=3")
    app.run(debug=True)
