from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from profiles.models import Profile
# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    #is_staff = serializers.CharField(source='user.is_staff')
    password = serializers.CharField(source='user.password')
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
        user = User.objects.create_user(username=user.get('username'), email= user.get('email'), password=user.get('password'))
        profile = Profile.objects.create(user=user,poi=attrs.get('poi'))
        #user = User.objects.create_user(username='stefano', email= 'essetizeta@gmail.com', password='yuyuyuyu')
        p = Profile(user=user)
        print p
        return Profile(user=user)