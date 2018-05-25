from django.contrib import admin
from .models import  UserProfile,UserGroup,GroupManager,GroupMember

admin.site.register(UserProfile)
admin.site.register(UserGroup)
admin.site.register(GroupManager)
admin.site.register(GroupMember)