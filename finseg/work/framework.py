#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pw @ 2016-05-27 15:07:19
@author xiehui
"""

import os
import zerorpc
import ConfigParser
import time
import lib.loggingmodule
import lib.tderr
import json

import jieba
import jieba.posseg
import jieba.analyse


class Framework(object):
    def __init__(self):
        """init"""

        self.config = ConfigParser.ConfigParser()
        self.log_module = lib.loggingmodule.LoggingModule()
        self.config_file = lib.path.path("ROOT_DIR").abspath("conf/local.ini")

    def load(self):
        """Load config file"""
        
        self.log_module.info("load config start")
        if len(self.config.read(self.config_file)) == 0:
            self.log_module.error("load config file %s failed!" % self.config_file)
            return lib.tderr.TD_ERROR_FAILTRUE

        sougou_file_path = lib.path.path("ROOT_DIR").abspath(self.config.get("task", "sougou_finance_dict"))
        #sougou_file = file(sougou_file_path, "r")
        #for line in sougou_file.readlines():
            #print line.strip().split(" ")[1]
        jieba.load_userdict(sougou_file_path)

        return lib.tderr.TD_OK

    def start_service(self):
        """startService"""

        self.log_module.info("start service start")

        print "start"
        rpc_server = zerorpc.Server(self)
        ip_port = self.config.get("task", "port")
        rpc_server.bind("tcp://0.0.0.0:" + ip_port)
        rpc_server.run()

    def start(self):
        """start"""

        rv = self.load()
        if lib.tderr.FAILED(rv):
            return rv

        rv = self.start_service()
        if lib.tderr.FAILED(rv):
            return rv

    def process(self, query):
        """Start the process"""
        self.log_module.info("start process")
        print "quer:", query
        query = query.strip()

        rv = self.load()
        input_data = {}

        #seg_list = jieba.cut(query, cut_all=True)
        seg_list = jieba.cut(query, cut_all=False)
        ret_list = []
        for item in seg_list:
            item = item.strip()
            if len(item) > 0:
                ret_list.append(item)
        ret = "/ ".join(ret_list)
        return ret
        #return json.dumps(input_data["response"])
