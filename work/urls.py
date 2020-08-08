from django.urls import path

from work.views import work

urlpatterns = [
    path('', work, name='work'),
]
