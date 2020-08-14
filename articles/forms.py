from django import forms
from .models import Articles, Category, Comments
from django.contrib.auth.models import User

choices_category_of_article = Category.objects.all().values_list('name', 'name')


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'content', 'date', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Your title',
                                            'class': 'form-control '}),
            'content': forms.Textarea(attrs={'placeholder': 'Your article',
                                             'class': 'form-control form-control-lg'}),
            'category': forms.Select(choices=choices_category_of_article,
                                     attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'comment_text', 'article')
        widgets = {
            'author': forms.Select(attrs={'placeholder': 'Your name',
                                          'class': 'form-control'}),
            'comment_text': forms.Textarea(attrs={'placeholder': 'Your comment',
                                                  'class': 'form-control'})
        }
