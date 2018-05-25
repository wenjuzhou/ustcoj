from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserGroup,UserProfile,GroupMember,GroupManager

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('id','name','description','creator')
class UserCreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('id','name','description','creator','invite_key')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','user','sno')
class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = ('group','user')

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserRegister(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password", "date_joined")
