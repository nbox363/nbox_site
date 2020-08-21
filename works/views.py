from django.shortcuts import render
from articles.models import Category


def works(request):
    context = Category.objects.all()
    return render(request, 'works/works_page.html', {'categories': context})
