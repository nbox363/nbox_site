from django.db import models
from tinymce.models import HTMLField


class Articles(models.Model):
    title = models.CharField(max_length=120)
    content = HTMLField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
