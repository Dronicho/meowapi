from django.contrib.auth.models import User, Group
from django.db import models
# from .models import News
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = models.CharField(max_length=15)

    def create(self, data):
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )

        user.set_password(data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'password', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

#
# class NewsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = News
#         fields = ('url', 'pub_date', 'title', 'summary', 'tags')
