from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_protect
from models import News
from models import Report
from models import Research
from models import Marketoveriew

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
        tmp['url'] = item.url
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
        tmp['url'] = item.url
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
        tmp['url'] = item.url
        tmp['author'] = item.author
        tmp['category'] = item.category
        tmp['institution'] = item.institution
        tmp['pubtime'] = item.pubtime
        carry_data['research'].append(tmp)
    return render(request, "bigdata/index.html", carry_data)
@csrf_protect
def marketoveriew(request):
    carry_data = {'marketoveriew':[]}
    tot_co = Marketoveriew.objects.count()
    print tot_co
    per_co = 50

    page=0
    if request.GET:
        page=int(request.GET['page'])

    carry_data['has_previous'] = False
    if page > 0:
        carry_data['has_previous'] = True
        carry_data['previous_page_number'] = page - 1
    carry_data['has_next'] = False
    if tot_co > per_co * page:
        carry_data['has_next'] = True
        carry_data['next_page_number'] = page + 1
    for item in Marketoveriew.objects.order_by('-pubtime')[page*per_co:page*per_co+per_co]:
        tmp = {}
        tmp['title'] = item.title
        tmp['url'] = item.url
        tmp['author'] = item.author
        tmp['pubtime'] = item.pubtime
        carry_data['marketoveriew'].append(tmp)
    return render(request, "bigdata/index.html", carry_data)
