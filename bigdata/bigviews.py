#coding=utf-8
from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_protect
from models import News
from models import Report
from models import Research
from models import Marketoverview
from models import Morningpage
from models import Zqpage
from models import Eventstock

@csrf_protect
def index(request):
    carry_data = {'news':[]}
    tot_co = News.objects.count()
    per_co = 50

    page=0
    if request.GET:
        page=int(request.GET['page'])

    carry_data['has_previous'] = False
    carry_data['totnum'] = tot_co
    if page > 0:
        carry_data['has_previous'] = True
        carry_data['previous_page_number'] = page - 1
    carry_data['has_next'] = False
    if tot_co > per_co * page:
        carry_data['has_next'] = True
        carry_data['next_page_number'] = page + 1
    for item in News.objects.order_by('-pubtime')[page*per_co:page*per_co+per_co]:
        tmp = {}
        tmp['title'] = item.title
        tmp['url'] = "#"
        tmp['author'] = item.author
        tmp['pubtime'] = item.pubtime
        carry_data['news'].append(tmp)
    return render(request, "bigdata/index.html", carry_data)

@csrf_protect
def report(request):
    carry_data = {'report':[]}
    tot_co = Report.objects.count()
    per_co = 50

    page=0
    if request.GET:
        page=int(request.GET['page'])

    carry_data['has_previous'] = False
    carry_data['totnum'] = tot_co
    if page > 0:
        carry_data['has_previous'] = True
        carry_data['previous_page_number'] = page - 1
    carry_data['has_next'] = False
    if tot_co > per_co * page:
        carry_data['has_next'] = True
        carry_data['next_page_number'] = page + 1
    for item in Report.objects.order_by('-pubtime')[page*per_co:page*per_co+per_co]:
        tmp = {}
        tmp['title'] = item.title
        tmp['url'] = "#"
        tmp['category'] = item.category
        tmp['pubtime'] = item.pubtime
        carry_data['report'].append(tmp)
    return render(request, "bigdata/index.html", carry_data)

@csrf_protect
def research(request):
    carry_data = {'research':[]}
    tot_co = Research.objects.count()
    per_co = 50

    page=0
    if request.GET:
        page=int(request.GET['page'])

    carry_data['has_previous'] = False
    carry_data['totnum'] = tot_co
    if page > 0:
        carry_data['has_previous'] = True
        carry_data['previous_page_number'] = page - 1
    carry_data['has_next'] = False
    if tot_co > per_co * page:
        carry_data['has_next'] = True
        carry_data['next_page_number'] = page + 1
    for item in Research.objects.order_by('-pubtime')[page*per_co:page*per_co+per_co]:
        tmp = {}
        tmp['title'] = item.title
        tmp['url'] = "#"
        tmp['author'] = item.author
        tmp['category'] = item.category
        tmp['institution'] = item.institution
        tmp['pubtime'] = item.pubtime
        carry_data['research'].append(tmp)
    return render(request, "bigdata/index.html", carry_data)
@csrf_protect
def marketoverview(request):
    carry_data = {'marketoverview':[]}
    tot_co = Marketoverview.objects.count()
    print tot_co
    per_co = 50

    page=0
    if request.GET:
        page=int(request.GET['page'])

    carry_data['has_previous'] = False
    carry_data['totnum'] = tot_co
    if page > 0:
        carry_data['has_previous'] = True
        carry_data['previous_page_number'] = page - 1
    carry_data['has_next'] = False
    if tot_co > per_co * page:
        carry_data['has_next'] = True
        carry_data['next_page_number'] = page + 1
    for item in Marketoverview.objects.order_by('-pubtime')[page*per_co:page*per_co+per_co]:
        tmp = {}
        tmp['title'] = item.title
        tmp['url'] = "#"
        tmp['author'] = item.author
        tmp['pubtime'] = item.pubtime
        carry_data['marketoverview'].append(tmp)
    return render(request, "bigdata/index.html", carry_data)
@csrf_protect
def morningpage(request):
    carry_data = {'morningpage':[]}
    tot_co = Morningpage.objects.count()
    print tot_co
    per_co = 50

    page=0
    if request.GET:
        page=int(request.GET['page'])

    carry_data['has_previous'] = False
    carry_data['totnum'] = tot_co
    if page > 0:
        carry_data['has_previous'] = True
        carry_data['previous_page_number'] = page - 1
    carry_data['has_next'] = False
    if tot_co > per_co * page:
        carry_data['has_next'] = True
        carry_data['next_page_number'] = page + 1
    for item in Morningpage.objects.order_by('-pubtime')[page*per_co:page*per_co+per_co]:
        tmp = {}
        tmp['title'] = item.title
        tmp['url'] = "#"
        tmp['author'] = item.author
        tmp['pubtime'] = item.pubtime
        carry_data['morningpage'].append(tmp)
    return render(request, "bigdata/index.html", carry_data)
@csrf_protect
def zqpage(request):
    carry_data = {'zqpage':[]}
    tot_co = Zqpage.objects.count()
    print tot_co
    per_co = 50

    page=0
    if request.GET:
        page=int(request.GET['page'])

    carry_data['has_previous'] = False
    carry_data['totnum'] = tot_co
    if page > 0:
        carry_data['has_previous'] = True
        carry_data['previous_page_number'] = page - 1
    carry_data['has_next'] = False
    if tot_co > per_co * page:
        carry_data['has_next'] = True
        carry_data['next_page_number'] = page + 1
    for item in Zqpage.objects.order_by('-pubtime')[page*per_co:page*per_co+per_co]:
        tmp = {}
        tmp['title'] = item.title
        tmp['url'] = "#"
        tmp['author'] = item.author
        tmp['pubtime'] = item.pubtime
        carry_data['zqpage'].append(tmp)
    return render(request, "bigdata/index.html", carry_data)
@csrf_protect
def eventstock(request):
    print "start"
    carry_data = {'eventstock':[]}
    tot_co = Eventstock.objects.count()
    print tot_co
    per_co = 10

    page=0
    if request.GET:
        page=int(request.GET['page'])

    carry_data['has_previous'] = False
    carry_data['totnum'] = tot_co
    if page > 0:
        carry_data['has_previous'] = True
        carry_data['previous_page_number'] = page - 1
    carry_data['has_next'] = False
    if tot_co > per_co * page:
        carry_data['has_next'] = True
        carry_data['next_page_number'] = page + 1
    print "next:",carry_data['has_next']
    for item in Eventstock.objects.order_by('-pubtime')[page*per_co:page*per_co+per_co]:
        tmp = {}
        tmp['title'] = item.title
        if item.title.find("：") != -1:
        	tmp['title'] = item.title.split("：")[1]
        tmp['emotion'] = item.emotion
        tmp['url'] = "#"
        tmp['summary'] = item.summary
        tmp['pubtime'] = item.pubtime
        if len(item.stock_list) < 1:
            continue
        tmp['stock_list'] = " ".join(item.stock_list.split("\t")[0:6])
        print item.stock_list.split(" ")
        print item.stock_list.split("\t")
        carry_data['eventstock'].append(tmp)
    return render(request, "bigdata/eventstock.html", carry_data)
