from django.db import models
from submission.models import Submission
from markdownx.models import MarkdownxField

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone
# Create your models here.


class Judger(models.Model):

    name = models.CharField(max_length=100, blank=True)
    description = MarkdownxField(max_length=1000, blank=True)

    host = models.CharField(max_length=100, blank=True)
    token = models.CharField(max_length=100, blank=True)

    running_task_number = models.IntegerField(default=0)
    cpu_core = models.IntegerField(default=1)
    cpu_usage = models.FloatField(default=0.0)
    memory_usage = models.FloatField(default=0.0)

    act_time = models.DateTimeField(auto_now=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Submission)
def start_judge(sender, instance, created, **kwargs):
    if created:
        # TODO: put the submission into task queue
        instance.judge_start_time = timezone.now()
        instance.judge_finish_time = timezone.now()
        instance.status = 0
        instance.save()
