from .models import UserGroup,GroupMember,GroupManager

from users.serializers import UserGroupSerializer,UserProfileSerializer,UserSerializer,UserRegister,UserCreateGroupSerializer,GroupMemberSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login,login_required,logout
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

class UserGroupList(APIView):
    def get(self,request,format='json'):
        group = UserGroup.objects.all()
        serializer = UserGroupSerializer(group,many=True)
        return Response(serializer.data)

class CreateGroup(APIView):
    def post(self,request,format='json'):
        request.data['creator'] = request.user
        serializer = UserCreateGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class JoinGroup(APIView):
    def post(self,request,format='json'):
        request.data['user'] = '2'
        request.data['thegroup'] = UserGroup.objects.get(name=request.data['groupname'])
        request.data['group'] = request.data['thegroup'].pk
        serializer = GroupMemberSerializer(data=request.data)
        if serializer.is_valid():
            member_exist = GroupMember.objects.filter(group=request.data['group'],user=request.data['user'])
            if request.data['thegroup'].invite_key == request.data['invite_key']:
                if len(member_exist)==0:
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                return Response(data='you have been in the group\n',status=status.HTTP_400_BAD_REQUEST)
            return Response(data='invalid invite key\n',status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def LogIn(request):
    data = JSONParser().parse(request)
    user = authenticate(username=data['username'], password=data['password'])
    if user is not None:
        login(request,user)
        return HttpResponse(user)
    return HttpResponse(user)

@login_required
@csrf_exempt
def LogOut(request):
    #data = JSONParser().parse(request)
    #user = authenticate(username=data['username'], password=data['password'])
    #if user is not None:
    logout(request)
    #return HttpResponse('logged out')


class UserRegister(APIView):
    def post(self,request,format='json'):
        serializer = UserRegister(data=request.data)
        user_exist = User.objects.filter(username=serializer.data['username'])
        if len(user_exist)==0:
            user = User.objects.create_user(serializer.data['username'],serializer.data['email'], serializer.data['password'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                data='Username exist\n',
                status=status.HTTP_400_BAD_REQUEST,
            )
'''
class LogIn(APIView):
    @csrf_exempt
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            if user is not None:
                login(request, user)
                print("OK\n")
        print("Error\n")
'''