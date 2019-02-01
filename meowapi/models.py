from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import datetime


class Article(models.Model):
    url_to_source = models.CharField(max_length=200)
    title = models.TextField(max_length=5000, default='none')
    summary = models.TextField(max_length=10000, default='none')
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now)
    theme = models.CharField(max_length=100, default='none')


@receiver(models.signals.post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# create token for existing users if they have no one
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
