from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from profiles.models import Profile
from .models import Category
# Serializers define the API representation.


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
