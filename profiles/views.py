from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
from rest_framework import generics, permissions, authentication, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import Profile
from serializers import *
from .permissions import  IsProfileOwner



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

    
class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    
    
class ProfileDetails(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UpdateUserSerializer
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsProfileOwner,)
    

