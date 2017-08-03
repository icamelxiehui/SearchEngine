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

