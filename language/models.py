from django.db import models

# Create your models here.


class Language(models.Model):

    name = models.CharField(max_length=63)
    compiler_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' : ' + self.compiler_info