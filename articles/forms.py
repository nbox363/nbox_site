from django import forms
from .models import Articles


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'content', 'date')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Your title',
                                            'class': 'form-control '}),
            'content': forms.Textarea(attrs={'placeholder': 'Your article',
                                             'class': 'form-control form-control-lg'}),
            'date': forms.DateInput(attrs={'class': 'form-control'})
        }
