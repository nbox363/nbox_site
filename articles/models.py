from tinymce.models import HTMLField

from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Title',)
    content = HTMLField(verbose_name='Article text')
    date = models.DateTimeField(verbose_name='Publication date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comments(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Comment author')
    comment_text = models.CharField(max_length=400,
                                    verbose_name='Comment text')
    article = models.ForeignKey(Articles,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
