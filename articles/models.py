from django.db import models
from tinymce.models import HTMLField


class Articles(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Title',
        unique=True)
    content = HTMLField(verbose_name='Article text')
    date = models.DateTimeField(verbose_name='Publication date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        unique_together = ('title', 'date')


class Comments(models.Model):
    comment = models.CharField(max_length=400, verbose_name='Comment text')
    author = models.CharField(max_length=120, verbose_name='Comment author')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        unique_together = ('author', 'article')
