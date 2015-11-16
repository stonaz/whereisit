from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from profiles.models import Profile
from .models import Item
# Serializers define the API representation.


class ItemSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='owner.user.username',read_only=True)
    poi = serializers.CharField(source='owner.poi',read_only=True)
    category_name = serializers.CharField(source='category.name',read_only=True)


    class Meta:
        model = Item
        fields = ( 'category_name','username','poi','name', 'description','owner','category')