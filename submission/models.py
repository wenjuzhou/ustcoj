from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CODE = (
    # TODO : fill the code
    (0, 'Accepted'),
    (7, 'Pending'),
)


class Submission(models.Model):

    code = models.TextField()

    language = models.ForeignKey('language.Language')
    user = models.ForeignKey(User)
    problem = models.ForeignKey('problem.Problem')

    status = models.IntegerField(choices=STATUS_CODE, default=7)
    info = models.CharField(max_length=65535, blank=True)

    add_time = models.DateTimeField('time added', auto_now_add=True)
    judge_start_time = models.DateTimeField(blank=True)
    judge_finish_time = models.DateTimeField(blank=True)

    visible = models.BooleanField(default=True)
    share = models.BooleanField(default=False)

    class Meta:
        ordering = ['-add_time']

    def __str__(self):
        return str(self.pk) + ' (By ' + self.user.username + ')'
