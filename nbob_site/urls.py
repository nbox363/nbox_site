from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from articles.views import article_create_view

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', include('home.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('works/', include('works.urls')),
    path('create/', article_create_view, name='create'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
