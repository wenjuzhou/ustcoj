from django.db import models
import django.utils.timezone as timezone
from markdownx.models import MarkdownxField

# Create your models here.


class News(models.Model):

    title = models.CharField(max_length=100)

    category = models.CharField(max_length=50, blank=True)

    pub_time = models.DateTimeField('time to publish', default=timezone.now)
    mod_time = models.DateTimeField('time modified', auto_now=True)
    add_time = models.DateTimeField('time added', auto_now_add=True)

    content = MarkdownxField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-add_time']
        verbose_name_plural = "news"
