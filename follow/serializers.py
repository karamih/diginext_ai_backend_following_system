from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Follow
from user.serializers import UserSerializer

class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    following = UserSerializer(read_only=True)
    
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
        read_only_fields = ['created_at']



class DailyFollowersSerializer(serializers.Serializer):
    date = serializers.DateField()
    following = serializers.IntegerField()
    count = serializers.IntegerField()



class GetAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']