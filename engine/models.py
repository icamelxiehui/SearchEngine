from __future__ import unicode_literals

from django.db import models

# Create your models here.
class News(models.Model):
    url = models.TextField()
    image = models.TextField()
    title = models.TextField()
    content = models.TextField()
    author = models.TextField()
    website = models.TextField()
    description = models.TextField()
    pubtime = models.DateTimeField()

    def __str__(self):
        return self.title

