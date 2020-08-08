from django.contrib import admin
from django.urls import path, include

from articles.views import article_create_view

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', include('home.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('works/', include('works.urls')),
    path('create/', article_create_view, name='create'),

]
