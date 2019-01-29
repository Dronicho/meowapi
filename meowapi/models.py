from django.db import models


class Article(models.Model):
    url_to_source = models.CharField(max_length=200)
    title = models.TextField(max_length=5000, default='none')
    summary = models.TextField(max_length=10000, default='none')
    pub_date = models.DateTimeField('date published')
    # tags = ArrayField(models.CharField, size=10)
# Create your models here.
