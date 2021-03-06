from __future__ import unicode_literals

from django.db import models

# Create your models here.

from mongoengine import *
connect("big_data")
 
class News(Document):
    title = StringField(max_length=50)  
    url = StringField(max_length=50)  
    pubtime = DateTimeField()
    author = StringField(max_length=50)  
    website = StringField(max_length=50)  
    image= StringField(max_length=50)  
    content = StringField()
    description = StringField()
    meta = { 'collection': 'news'}

class Report(Document):
    title = StringField()  
    url = StringField()  
    category = StringField()
    website = StringField()
    pubtime = DateTimeField()
    content = StringField()
    meta = { 'collection': 'report'}

class Research(Document):
    title = StringField()  
    url = StringField()  
    author = StringField()  
    institution = StringField()
    website = StringField()
    category = StringField()
    pubtime = DateTimeField()
    content = StringField()
    meta = { 'collection': 'research'}
class Marketoverview(Document):
    title = StringField(max_length=50)  
    url = StringField(max_length=50)  
    pubtime = DateTimeField()
    author = StringField(max_length=50)  
    website = StringField(max_length=50)  
    image= StringField(max_length=50)  
    content = StringField()
    description = StringField()
    meta = { 'collection': 'market_overview'}

class Morningpage(Document):
    title = StringField(max_length=50)  
    url = StringField(max_length=50)  
    pubtime = DateTimeField()
    author = StringField(max_length=50)  
    website = StringField(max_length=50)  
    image= StringField(max_length=50)  
    content = StringField()
    description = StringField()
    meta = { 'collection': 'morning_page'}

class Zqpage(Document):
    title = StringField(max_length=50)  
    url = StringField(max_length=50)  
    pubtime = DateTimeField()
    author = StringField(max_length=50)  
    website = StringField(max_length=50)  
    image= StringField(max_length=50)  
    content = StringField()
    description = StringField()
    meta = { 'collection': 'zq_page'}

class Eventstock(Document):
    title = StringField(max_length=50)  
    url = StringField(max_length=50)  
    emotion = StringField(max_length=50)  
    pubtime = DateTimeField()
    summary = StringField(max_length=50)  
    stock_list= StringField(max_length=50)  
    meta = { 'collection': 'even_stock'}
