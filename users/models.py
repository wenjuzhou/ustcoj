from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sno = models.CharField(max_length=11,blank=True)
    group_create_permission = models.BooleanField(default=0)
    connect_way = models.CharField(max_length=100,blank=True)

class UserGroup(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=500,blank=True)
    creator = models.ForeignKey(UserProfile,related_name='created',on_delete=models.CASCADE)
    invite_key = models.CharField(max_length=20)
    manager = models.ManyToManyField(UserProfile,through='GroupManager',through_fields=('group','user'),related_name='managed')
    member = models.ManyToManyField(UserProfile,through='GroupMember',through_fields=('group','user'),related_name='jonit')
    def Save(self,*args,**kwargs):
        super(UserGroup,self).save(*args,**kwargs)
class GroupManager(models.Model):
    group = models.ForeignKey(UserGroup,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
class GroupMember(models.Model):
    group = models.ForeignKey(UserGroup,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
