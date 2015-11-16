from django.conf.urls import patterns, url
from .views import *


urlpatterns = [
    url(r'^$', CategoriesListCreate.as_view(), name='api_categories_list_create'),
    url(r'^(?P<name>[-\w]+)/items/$', CategoryItemsList.as_view(), name='api_categories_items_list'),
]