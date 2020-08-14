from django.urls import path

from .views import ArticleView, ArticlesView, CreateArticleView, AddCommentView, category_view

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles'),
    path('<int:pk>/', ArticleView.as_view(), name='article'),
    path('create/', CreateArticleView.as_view(), name='create'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('category/<str:category_name>/', category_view, name='category'),
]
