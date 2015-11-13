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


# Create your views here.

class ItemsListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
