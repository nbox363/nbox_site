from django.contrib.auth.models import User
from django.db import models

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Articles(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Title')
    content = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='life')
    date = models.DateTimeField(verbose_name='Publication date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comments(models.Model):
    article = models.ForeignKey(Articles,
                                related_name='comments',
                                on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=400)

    def __str__(self):
        return (str(self.article) + ' | ' + str(self.author) +
                ' | ' + str(self.comment_text)[:23])

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'





