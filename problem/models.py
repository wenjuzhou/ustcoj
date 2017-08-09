from django.db import models
from markdownx.models import MarkdownxField
from jsonfield import JSONField
import django.utils.timezone as timezone

# Create your models here.


class ProblemTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AbstractProblem(models.Model):
    title = models.CharField(max_length=255)
    description = MarkdownxField()

    input_description = MarkdownxField()
    output_description = MarkdownxField()
    hint = MarkdownxField()
    samples = JSONField()

    input_method = models.CharField(max_length=31, default='stdin')
    output_method = models.CharField(max_length=31, default='stdout')
    time_limit = models.IntegerField("time limit (ms)", default=1000)
    memory_limit = models.IntegerField('memory limit (MB)', default=256)
    testset_id = models.CharField(max_length=255)

    tags = models.ManyToManyField(ProblemTag)
    source = models.CharField(max_length=255, blank=True)

    pub_time = models.DateTimeField('time to publish', default=timezone.now)
    mod_time = models.DateTimeField('time modified', auto_now=True)
    add_time = models.DateTimeField('time added', auto_now_add=True)

    public = models.BooleanField(default=False)

    special_judge = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Problem(AbstractProblem):

    problem_id = models.IntegerField(unique=True, db_index=True)

    def __str__(self):
        return str(self.problem_id) + '-' + self.title

    class Meta:
        ordering = ['problem_id']