from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from jsonfield import JSONField

from problem.models import AbstractProblem

from django.contrib.auth.models import User
# Create your models here.


class AbstractContest(models.Model):

    name = models.CharField(max_length=255)
    description = MarkdownxField()

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    creator = models.ForeignKey(User)
    managers = models.ManyToManyField(User, related_name='managed_contest_set')
    players = models.ManyToManyField(User,
                                     related_name='joined_contest_set',
                                     through='PlayerInfo',
                                     )

    pub_time = models.DateTimeField('time to publish', default=timezone.now)
    mod_time = models.DateTimeField('time modified', auto_now=True)
    add_time = models.DateTimeField('time added', auto_now_add=True)

    class Meta:
        abstract = True

    def get_managers(self):
        return self.managers.all()

    def get_players(self):
        return self.players.all()


class PlayerInfo(models.Model):
    contest = models.ForeignKey('Contest')
    player = models.ForeignKey(User)

    info = JSONField()

    reg_time = models.DateTimeField(auto_now_add=timezone.now)


class Contest(AbstractContest):

    def get_info(self, user: User):
        player_info = PlayerInfo.objects.get(contest=self, player=user)
        if player_info is None:
            return None
        else:
            return player_info.info

    def set_info(self, user: User, info):
        player_info = PlayerInfo.objects.get(contest=self, player=user)
        if player_info is None:
            return False
        else:
            player_info.info = info
            player_info.save()
            return True

    def is_running(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time


class ContestProblem(AbstractProblem):

    contest = models.ForeignKey(Contest, related_name='problem_set')
    index = models.CharField(max_length=15)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ['index']

