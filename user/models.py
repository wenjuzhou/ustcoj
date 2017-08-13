from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=32, default='', blank=True)
    # Student ID or Staff ID
    sno = models.CharField(max_length=11, default='', blank=True, editable=False)

    def __str__(self):
        return self.user.username

    def get_avatar_url(self, size=40):
        """
        Get user's gravatar url
        :return:
        """
        import hashlib
        import urllib.parse

        email = self.user.email.encode('utf-8')
        gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()
        gravatar_url += '?' + urllib.parse.urlencode({'s': str(size)})

        return gravatar_url


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class UserGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = MarkdownxField(blank=True)

    creator = models.ForeignKey(User, related_name='created_groups')
    managers = models.ManyToManyField(User, related_name='managed_groups')
    members = models.ManyToManyField(User, related_name='joined_groups')

    public = models.BooleanField(default=False)

    add_time = models.DateTimeField('time added', auto_now_add=True)

    def __str__(self):
        return self.name
