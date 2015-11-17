from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, status
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

from profiles.models import Profile
from categories.models import Category
# Serializers define the API representation.

def check_passwd(password,confirm_password):
        print(password)
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(    validators=[UniqueValidator(queryset=Profile.objects.all())])
    #is_staff = serializers.CharField(source='user.is_staff')
    password = serializers.CharField(source='user.password', write_only=True)
    confirm_password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
        model = Profile
        fields = ('poi', 'username', 'email','password','confirm_password')
        
    
        
    def create(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.user.email = attrs.get('user.email', instance.user.email)
            instance.poi = attrs.get('poi', instance.poi)
            instance.user.password = attrs.get('user.password', instance.user.password)
            return instance
        print attrs
        user = attrs.get('user')
        confirm_password = attrs.get('confirm_password')
        password = user.get('password')
        if password != confirm_password:
            raise serializers.ValidationError('Password confirmation mismatch')
        
        check_passwd(password,confirm_password)
        user = User.objects.create_user(username=user.get('username'), email= user.get('email'), password=user.get('password'))
        profile = Profile.objects.create(user=user,poi=attrs.get('poi'),email=attrs.get('email'))
        p = Profile(user=user)
        print p
        return Profile(user=user)
    
    def update(self, instance, attrs):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        raise serializers.ValidationError('method not valid')
        print attrs
        if instance is not None:
            user = attrs.get('user')
            print instance.user.email
            instance.user.email = 'pippo@topolinia.net'
            instance.poi = attrs.get('poi', instance.poi)
            instance.user.password = attrs.get('user.password', instance.user.password)
            print instance.user.email
            instance.save()
            return instance
        print attrs
        user = attrs.get('user')
        user = User.objects.create_user(username=user.get('username'), email= user.get('email'), password=user.get('password'))
        profile = Profile.objects.create(user=user,poi=attrs.get('poi'))
        p = Profile(user=user)
        print p
        return Profile(user=user)
    
class UpdateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    #poi = serializers.CharField(allow_blank=True)
    email = serializers.EmailField(    validators=[UniqueValidator(queryset=Profile.objects.all())])
    ##is_staff = serializers.CharField(source='user.is_staff')
    #password = serializers.CharField(source='user.password', write_only=True)
    #confirm_password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
        model = Profile
        fields = ('poi', 'username', 'email')
        
