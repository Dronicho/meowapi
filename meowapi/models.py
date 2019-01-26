from django.db import models
from django.contrib.postgres.fields import ArrayField


class News(models.Model):
    url = models.CharField(max_length=200)
    title = models.TextField(max_length=200, default='none')
    summary = models.TextField(max_length=500, default='none')
    pub_date = models.DateTimeField('day published')
    # tags = ArrayField(models.CharField, size=10)
# Create your models here.
