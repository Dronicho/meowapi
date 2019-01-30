from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

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


class get_articles_by_theme(APIView):
    """
    View to get news by theme name
    """

    def get(self, theme, format=None):
        articles = Article.objects.filter(theme=theme)
        return Response(articles)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

