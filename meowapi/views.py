from django.contrib.auth.models import User, Group
from .models import News
from rest_framework import viewsets
from meowapi.serializers import UserSerializer, GroupSerializer#, NewsSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#
# class NewsViewSet(viewsets.ModelViewSet):
#     """
#     API to view and edit news
#     """
#     queryset = News.objects.all().order_by('-pub_date')
#     serializer_class = NewsSerializer


