#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File Name: search_views.py
Author: xiehui
mail: 372623335@qq.com
Created Time: 六  7/15 09:58:19 2017
"""

from haystack.views import SearchView  
from .models import *  
import zerorpc
import json
import requests
import datetime
import logging
from django.shortcuts import render

class MySeachView(SearchView):  
    def __init__(self): 
        SearchView.__init__(self) 

    def get_results(self):
        result = super(MySeachView,self).get_results().order_by("-pubtime")
        return result

    def get_context(self):
        context = super(MySeachView,self).get_context()  
        query = context['query'].strip()
        logger = logging.getLogger('django')

        if query and len(context['page'].object_list) < 1:
            #c = zerorpc.Client()
            #c.connect("tcp://127.0.0.1:4242")
            #ret = json.loads(c.process(query.encode('utf-8')))
            try:
                ret = json.loads(requests.post("http://127.0.0.1:5001",params={'query':query.encode('utf-8')}).text)
                context['othersearch'] = ret
            except Exception as err:
                logger.error("[request_sofa_error:%s]" % err)

        logger.info("[query:%s]" % query)
        return context

class MyTestView(SearchView):  
    def __init__(self): 
        SearchView.__init__(self) 

    def get_results(self):
        result = super(MyTestView,self).get_results().order_by("-pubtime")
        return result

    def get_context(self):
        context = super(MyTestView,self).get_context()  
        query = context['query'].strip()
        logger = logging.getLogger('django')
        context['page'].object_list = []

        if query and len(context['page'].object_list) < 1:
            #c = zerorpc.Client()
            #c.connect("tcp://127.0.0.1:4242")
            #ret = json.loads(c.process(query.encode('utf-8')))
            try:
                ret = json.loads(requests.post("http://127.0.0.1:5001",params={'query':query.encode('utf-8')}).text)
                context['othersearch'] = ret
            except Exception as err:
                logger.error("[request_sofa_error:%s]" % err)

        logger.info("[query:%s]" % query)
        return context
    def create_response(self):
        """
        Generates the actual HttpResponse to send back to the user.
        """

        context = self.get_context()

        return render(self.request, "search/test.html", context)


