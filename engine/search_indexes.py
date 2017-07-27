#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File Name: search_indexes.py
Author: xiehui
mail: 372623335@qq.com
Created Time: 六  7/15 10:03:12 2017
"""

import datetime
from haystack import indexes
from engine.models import News

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #author = indexes.CharField(model_attr='user')
    #pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
       # return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
