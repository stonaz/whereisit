from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf.urls import patterns, include, url

from rest_framework import routers, serializers, viewsets
from rest_framework import generics, permissions, authentication, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Item
from serializers import *
from .permissions import IsOwnerOrReadOnly


# Create your views here.

class ItemsListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = (authentication.SessionAuthentication,)
    
    def perform_create(self, serializer):
        """ determine user when node is added """
        if serializer.instance is None:
            profile = Profile.objects.get(user=self.request.user)
            #print profile
            serializer.save(owner=profile)
    
class ItemsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemUpdateSerializer
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    
