from django.contrib.auth.models import User, Group
from django.db import models
from .models import Article
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = models.CharField(max_length=15)

    def create(self, data):
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=data['password']
        )

        user.set_password(data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        write_only_fields = ('password',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
