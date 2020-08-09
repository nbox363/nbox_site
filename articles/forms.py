from django import forms

import datetime

from .models import Articles


class ArticlesForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your title'
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your article'
            }
        )
    )

    date = forms.DateField(initial=datetime.datetime.now())
