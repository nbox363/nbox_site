from django.shortcuts import render
from articles.models import Category
from .gun import main


def home(request):
    context = Category.objects.all()
    game = main
    return render(request, 'home/home_page.html', {'categories': context, 'game': game})


def about(request):
    context = Category.objects.all()
    return render(request, 'home/about.html', {'categories': context})


def wrapper(request):
    context = Category.objects.all()
    return render(request, 'home/wrapper.html', {'categories': context})
