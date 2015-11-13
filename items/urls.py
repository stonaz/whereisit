from django.conf.urls import patterns, url
from .views import *


urlpatterns = [
    url(r'^$', ItemsListCreate.as_view(), name='api_items_list_create'),
    #url(r'^(?P<pk>[0-9]+)/$', ProfileDetails.as_view(), name='api_profile_details'),
]