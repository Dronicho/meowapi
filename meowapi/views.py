from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

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

