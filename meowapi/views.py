from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.authtoken.models import Token

from meowapi.serializers import UserSerializer, GroupSerializer, ArticleSerializer
from .models import Article


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


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API to view and edit news
    """
    queryset = Article.objects.all().order_by('-pub_date')
    serializer_class = ArticleSerializer

    @action(methods=['get'], detail=False, url_path='theme/(?P<theme>[a-z0-9]+)', name='theme')
    def get_articles_by_theme(self, request, theme=None):
        articles = Article.objects.filter(theme=theme).order_by('-pub_date')
        c = {
            'request': request
        }
        serializer = self.serializer_class(articles, many=True, context=c)

        return Response(serializer.data)


class RecommendView(APIView, RetrieveModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer

    def get(self, pk):
        return 'WOW'


class get_user_info(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, requset):
        c = {
            'requset': requset
        }
        user = Token.objects.get(key=requset.auth).user
        serializer = UserSerializer(user, context=c)
        return Response(serializer.data)