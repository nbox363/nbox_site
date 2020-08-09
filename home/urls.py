from django.urls import path

from . import views


urlpatterns = [
    path('about_me/', views.about, name='about'),
    path('', views.home, name="home"),
]
