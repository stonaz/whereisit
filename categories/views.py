from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf.urls import patterns, include, url

from rest_framework import routers, serializers, viewsets
from rest_framework import generics, permissions, authentication, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category
from serializers import *

from items.views import ItemsListCreate


# Create your views here.

class CategoriesListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryItemListMixin(object):
    category = None

    def get_category(self):
        """ retrieve category from DB """
        if self.category:
            return
        try:
            self.category = Category.objects.get(name=self.kwargs['name'])
        except Category.DoesNotExist:
            raise Http404(_('Category not found'))

    def get_queryset(self):
        """ extend parent class queryset by filtering items of the specified category """
        self.get_category()
        return super(CategoryItemListMixin, self).get_queryset().filter(category_id=self.category.id)

    def get_items(self, request, *args, **kwargs):
        # ListSerializerMixin.list returns a serializer object
        return (self.list(request, *args, **kwargs)).data

    def get(self, request, *args, **kwargs):
        """ Retrieve list of items of the specified category """
        self.get_category()
        # get items of category
        items = self.get_items(request, *args, **kwargs)
        content = CategorySerializer(self.category, context=self.get_serializer_context()).data
        content['items'] = self.get_items(request, *args, **kwargs)
        return Response(content)
    
    
class CategoryItemsList(CategoryItemListMixin, ItemsListCreate):
    """
    Retrieve list of items of the specified category
    Parameters:
     * `search=<word>`: search <word> in name of nodes of specified layer
     * `limit=<n>`: specify number of items per page (defaults to 40)
    """
    pass
