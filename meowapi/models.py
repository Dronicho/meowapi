from django.db import models
import datetime


class Article(models.Model):
    url_to_source = models.CharField(max_length=200)
    title = models.TextField(max_length=5000, default='none')
    summary = models.TextField(max_length=10000, default='none')
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now)
    theme = models.CharField(max_length=100, default='none')
# Create your models here.
