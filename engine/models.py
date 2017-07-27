from __future__ import unicode_literals

from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
  #  pubtime = models.DateTimeField()

    def __str__(self):
        return self.title

