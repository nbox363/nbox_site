from django.urls import path

from .views import ArticleView, ArticlesView, CreateArticleView

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles'),
    path('<int:pk>/', ArticleView.as_view(), name='article'),
    path('create/', CreateArticleView.as_view(), name='create'),
]
