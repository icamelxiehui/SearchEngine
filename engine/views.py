# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from models import *
import json
import zerorpc
import requests

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

@csrf_protect
def index(request):
    carry_data = {}
    return render(request, "index.html", carry_data)


def textseg(request):
    carry_data ={}
    if request.POST:
        query = request.POST['q'].strip()
        #c = zerorpc.Client()
        #c.connect("tcp://127.0.0.1:4243")
        #ret = c.process(query.encode('utf-8'))
        print "111"
        ret = requests.post("http://127.0.0.1:5000",params={'query':query}).text
        print "ret:", ret
        ret = ret.strip("/")
        carry_data["query"] = query
        carry_data["content"] = ret
        return render(request, "textseg.html", carry_data)
    else:
         return render(request, "textseg.html", carry_data)

def emotion(request):
    carry_data ={}
    if request.POST:
        query = request.POST['q'].strip()
        #c = zerorpc.Client()
        #c.connect("tcp://127.0.0.1:4243")
        #ret = c.process(query.encode('utf-8'))
        ret = requests.post("http://127.0.0.1:5000",params={'query':query}).text
        print "ret1:", ret
        carry_data["content"] = ret.strip("/")
        res = requests.post("http://127.0.0.1:5004",params={'query':ret.encode('utf-8')}).text
        print "ret2:", res
        carry_data["query"] = query
        carry_data["emotion"] = res
        return render(request, "emotion.html", carry_data)
    else:
         return render(request, "emotion.html", carry_data)

def newsread(request):
    carry_data ={}
    if request.POST:
        query = request.POST['q'].strip()
        res = requests.post("http://127.0.0.1:5005",params={'query':query}).text
        data = json.loads(res)
        carry_data["query"] = query
        carry_data["summary"] = data['summary']
        carry_data["emotion"] = data['emotion']
        carry_data["title"] = data['title']
        carry_data["content"] = data['content']
        carry_data["stock_list"] = data['stock_list']
        return render(request, "newsreader.html", carry_data)
    else:
         return render(request, "newsreader.html", carry_data)
