from django.urls import path

from .models import Articles
from .views import ArticleView, ArticlesView

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles'),

    path('<int:pk>/', ArticleView.as_view(), name='article'),
]
