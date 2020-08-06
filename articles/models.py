from django.db import models
from django.core import validators


class Articles(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
